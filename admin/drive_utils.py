# main_bot/admin/drive_utils.py
import os
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from config import GOOGLE_DRIVE_FOLDER_ID  # ID папки в твоём My Drive

# мы запускаем админку из папки admin/, а token лежит уровнем выше
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(BASE_DIR, 'token.pickle')

SCOPES = ["https://www.googleapis.com/auth/drive.file"]  # доступ только к файлам приложения

def _load_creds():
    if not os.path.exists(TOKEN_PATH):
        raise RuntimeError(
            "Не найден token.pickle. Сначала запусти auth_once.py в корне проекта и авторизуйся."
        )
    with open(TOKEN_PATH, "rb") as f:
        creds = pickle.load(f)
    # обновим при необходимости
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return creds

def _service():
    creds = _load_creds()
    return build("drive", "v3", credentials=creds)

def upload_file_to_drive(file_path: str, file_name: str, folder_id: str | None = None, make_public: bool = True) -> str:
    """
    Загружает файл в Google Drive, возвращает file_id.
    По умолчанию — в папку GOOGLE_DRIVE_FOLDER_ID и делает файл доступным по ссылке.
    """
    folder_id = folder_id or GOOGLE_DRIVE_FOLDER_ID
    svc = _service()

    metadata = {"name": file_name}
    if folder_id:
        metadata["parents"] = [folder_id]

    media = MediaFileUpload(file_path, resumable=True)
    created = svc.files().create(
        body=metadata,
        media_body=media,
        fields="id, webViewLink"
    ).execute()

    file_id = created["id"]

    if make_public:
        # читается по ссылке без входа — нужно, чтобы Telegram мог скачивать
        svc.permissions().create(
            fileId=file_id,
            body={"type": "anyone", "role": "reader"}
        ).execute()

    return file_id
