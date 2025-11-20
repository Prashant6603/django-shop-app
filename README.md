🗺️ GeoShop Locator – Django + Leaflet Geolocation App

An interactive geospatial web application built with Django, LeafletJS, and OpenStreetMap.
Users can add, update, delete, and view shops on a live map with search + filters + authentication.

🚀 Features
🔐 Authentication

User Signup

User Login

Secure Logout (POST method)

🏪 Shop Management

Add shops with:

Name

Address

Category

Latitude & Longitude (auto-filled on map-click)

Update shop information

Delete shops

View your shops in a clean table interface

🗺️ Interactive Map (Leaflet)

Map rendered via LeafletJS

Click to capture coordinates

Existing markers appear during edit

Dashboard shows all shops with markers & popups

🔍 Search & Filters

Search by name or address

Filter by category

Toggle between:

Your shops only

All shops



🗂️ Project Structure
geoshop/
│── shop/                 # App (views, models, forms, urls)
│── shops/                # Project settings
│── templates/            # HTML Templates
│── db.sqlite3            # Database
│── manage.py
│── requirements.txt
│── README.md

🛠️ Installation & Setup
1️⃣ Clone the repository
git clone <your-repo-url>
cd geoshop

2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate virtual environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Apply database migrations
python manage.py migrate

6️⃣ Run the development server
python manage.py runserver


Open in your browser:

http://127.0.0.1:8000/

🧰 Tech Stack
Backend

Django 5

SQLite (default)

Frontend

Bootstrap 5

LeafletJS

HTML / CSS / JavaScript


