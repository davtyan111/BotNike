import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # 👈 must be first!

from flask import Flask, render_template, request, redirect, url_for, session
from database.db import get_all_tariffs, get_all_locations, get_all_subcodes
from drive_utils import upload_file_to_drive
from database.db import insert_photo
from database.init import init_db
from config import GOOGLE_DRIVE_FOLDER_ID  # ✅ this should now work
from database.db import get_all_tariffs, add_tariff, delete_tariff

# --- Flask init ---
app = Flask(__name__)
app.secret_key = "my_super_secret_key"

# --- Авторизация ---
USERNAME = "admin"
PASSWORD = "pass123"

# --- Инициализация базы ---
init_db()

# --- Роуты ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return "❌ Неверный логин или пароль"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.before_request
def require_login():
    allowed_routes = ['login', 'static']
    if not session.get('logged_in') and request.endpoint not in allowed_routes:
        return redirect(url_for('login'))

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    tariff = request.form.get('tariff')
    location = request.form.get('location')
    subcode = request.form.get('subcode')

    if not file or not tariff or not location or not subcode:
        return "❌ Все поля обязательны!"

    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", file.filename)
    file.save(file_path)

    drive_id = upload_file_to_drive(file_path, file.filename)
    insert_photo(drive_id, tariff, location, subcode)

    os.remove(file_path)
    session['message'] = "✅ Файл успешно загружен!"
    return redirect(url_for('index'))

# Аналогично для locations и subcodes

@app.route('/tariffs', methods=['GET', 'POST'])
def manage_tariffs():
    if request.method == 'POST':
        if 'add' in request.form:
            name = request.form.get('tariff_name')
            add_tariff(name)
        elif 'delete' in request.form:
            id = request.form.get('delete')
            delete_tariff(id)
    return render_template('manage_tariffs.html', tariffs=get_all_tariffs())


@app.route('/')
def index():
    tariffs = get_all_tariffs()
    locations = get_all_locations()
    subcodes = get_all_subcodes()
    return render_template('index.html', tariffs=tariffs, locations=locations, subcodes=subcodes)



from database.db import get_all_locations, add_location, delete_location

@app.route('/locations', methods=['GET', 'POST'])
def manage_locations():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            add_location(name)
        return redirect(url_for('manage_locations'))
    
    locations = get_all_locations()
    return render_template('locations.html', locations=locations)

@app.route('/locations/delete/<int:id>')
def delete_location_route(id):
    delete_location(id)
    return redirect(url_for('manage_locations'))


from database.db import get_all_subcodes, add_subcode, delete_subcode

from database.db import get_all_subcodes, add_subcode, delete_subcode

@app.route('/subcodes', methods=['GET', 'POST'])
def manage_subcodes():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            add_subcode(name)
        return redirect(url_for('manage_subcodes'))

    subcodes = get_all_subcodes()
    return render_template('subcodes.html', subcodes=subcodes)

@app.route('/subcodes/delete/<int:id>')
def delete_subcode_route(id):
    delete_subcode(id)
    return redirect(url_for('manage_subcodes'))


if __name__ == '__main__':
    app.run(debug=True)
