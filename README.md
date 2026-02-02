# Technical Test – Junior Programmer (FastPrint)

A simple web application for product data management integrated with the FastPrint external API.  
This application is built using **Django (Python)** and implements **CRUD operations**, **automatic data synchronization**, and **input validation**.

---

## 📋 Main Features

- **Auto API Sync**  
  Automatic script (Django Management Command) for authentication and fetching product data from the FastPrint API using a dynamic password.

- **CRUD System**  
  Create, Read, Update, and Delete product data.

- **Smart Filtering**  
  The main page displays only products with status **"bisa dijual"**.

- **Data Validation**  
  Prevents negative price input and ensures required fields are filled.

- **Security**  
  Confirmation alert before deleting data.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.10+, Django 4.x  
- **Database**: PostgreSQL (SQLite used for development)  
- **Frontend**: HTML5, Bootstrap 5 (CDN)  
- **Libraries**:
  - requests
  - hashlib

---

## 🚀 Installation & Running the Project

### 1. Clone Repository
```bash
git clone https://github.com/your-username/test-fastprint.git
cd test-fastprint
```

### 2. Setup Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:
```bash
pip install django requests psycopg2-binary
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Data Synchronization (IMPORTANT)
```bash
python manage.py pull_data
```

This command will:
- Generate dynamic username & password based on server time
- Fetch product data from FastPrint API
- Store the data into the local database

### 6. Run Development Server
```bash
python manage.py runserver
```

Access the application at:
```
http://127.0.0.1:8000
```

---

## 📷 Demo & Documentation

**Application Flow:**

- **Main Page**  
  Displays filtered product table (only status **"bisa dijual"**).

- **Add / Edit Product**  
  Uses Django form validation.  
  Price must be a positive number.

- **Delete Product**  
  Uses JavaScript `confirm()` to prevent accidental deletion.

Demo Video:  
`[Insert YouTube / Google Drive link here]`

---

## 📂 Project Structure

```text
test_fastprint/
├── manage.py
├── fastprint_core/          # Project settings and main URLs
├── products/                # Main application
│   ├── management/
│   │   └── commands/
│   │       └── pull_data.py   # Custom API sync script
│   ├── models.py            # Database schema
│   ├── views.py             # Controller logic
│   ├── forms.py             # Form validation
│   └── templates/           # HTML templates
```

---

## 📝 Developer Notes

- **API Authentication**  
  The `pull_data.py` script generates a dynamic MD5 password using the format:
  ```
  bisacoding-d-m-y
  ```

- **Data Handling**  
  Product prices from the API are sanitized before being saved to the database to avoid issues with non-numeric characters.

---

## 👤 Author

Name: Timothy
Email: timspeed007@gmail.com
