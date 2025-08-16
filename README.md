# Application Setup Guide

## Overview
This is a Telegram bot application with an admin panel for managing photos, tariffs, locations, and subcodes. The application uses MySQL as the primary database and includes Google Drive integration.

## Prerequisites
- Python 3.7+
- MySQL Server
- Google Cloud Console credentials (for Drive API)
- Telegram Bot Token

## Quick Start Guide

### 1. Database Setup (MySQL)

#### Install MySQL (if not already installed)
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mysql-server mysql-client

# macOS (using Homebrew)
brew install mysql
brew services start mysql

# Windows
# Download and install from https://dev.mysql.com/downloads/installer/
```

#### Create Database and User
```bash
# Login to MySQL as root
sudo mysql -u root

# Create database
CREATE DATABASE IF NOT EXISTS photo_bot_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Create user with password
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'secret';

# Grant privileges
GRANT ALL PRIVILEGES ON photo_bot_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

# Exit MySQL
EXIT;
```

#### Create Tables
```bash
# Connect to database
mysql -u root -psecret photo_bot_db

# Run these SQL commands to create tables:
CREATE TABLE IF NOT EXISTS photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drive_file_id VARCHAR(255) NOT NULL,
    tariff VARCHAR(50),
    location VARCHAR(50),
    subcode VARCHAR(50),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Application Setup
- Clone the repository and navigate to the project directory.
- Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Running the Application
- Start the application by running:
```bash
python admin/app.py
```

### 4. Accessing the Admin Panel
- Open your web browser and navigate to `http://localhost:5000/login`.
- Use the following credentials to log in:
  - Username: `admin`
  - Password: `pass123`
