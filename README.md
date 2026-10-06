# Prazoo – Django Web Application

Prazoo is a web application developed using **Python and Django**. It includes multiple pages for presenting services, designs, company information, contact details, and user signup functionality.

## Features

* Responsive home page
* About page
* Services page
* Design page
* Contact page
* User signup functionality
* Django template-based frontend
* SQLite database integration
* Static image and asset management
* Django admin panel
* Database migrations

## Technologies Used

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **JavaScript**
* **SQLite**
* **Git & GitHub**

## Project Structure

```text
prazoo-django/
│
├── bob/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── jaibabu/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Gnaneswari0603/prazoo-django.git
```

### 2. Navigate to the project directory

```bash
cd prazoo-django
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Database

The application uses **SQLite** for local development. The database file is excluded from version control through `.gitignore`.

## Author

**Gnaneswari**

GitHub: [Gnaneswari0603](https://github.com/Gnaneswari0603)
