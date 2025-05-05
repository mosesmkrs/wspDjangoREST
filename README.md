# Hotel Reservation API

**A Django REST Framework API for managing hotel bookings**

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 3.2+
- Django REST Framework

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/yyyy.git
cd yyy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install django djangorestframework

#Database Setup
python manage.py makemigrations
python manage.py migrate

#Running the Server
python manage.py runserver