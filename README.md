# Donate2Dine 🍽️

Donate2Dine is a web-based application built using the Django framework designed to manage and facilitate food donations. It serves as a vital bridge between generous **Donors** (who have surplus food) and **Acceptors** (who require food), promoting food sharing and community support.

---

## 🌟 Key Features

### 1. Role-Based System
- **Donors**: Can seamlessly add, update, and manage surplus food availability.
- **Acceptors**: Can search for available food in their local area, review donor details, and claim items.
- Specific dashboards tailored to each role ensure a streamlined user experience.

### 2. Comprehensive Food Management
- Donors list food specifying details like food name, quantity, pick-up location, available time, and contact info.
- Acceptors can track their "Claims" and view detailed information. 
- Integrated status system (Available -> Claimed).

### 3. Integrated Messaging System
- Secure, in-app chat platform allowing Donors and Acceptors to communicate directly.
- Discuss pickup coordination without needing to immediately share external or private contact methods.
- Message history is stored safely within the database.

### 4. Admin Panel & Moderation
- Fully integrated with Django's built-in administration panel.
- Allows administrators to manage all users, monitor platform activity, delete inappropriate food listings, and intervene in chats if necessary.

---

## 🛠️ Technology Stack

- **Backend**: Python, Django Framework (v3.2)
- **Frontend**: HTML5, Vanilla Custom CSS, Bootstrap 5.3 Framework
- **Database**: SQLite (default configuration, easily translatable to PostgreSQL/MySQL)
- **Styling**: Responsive Design, Modern Dark Mode UI with Glassmorphism aesthetic.

---

## 🚀 Getting Started (Run Locally)

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/samalaakshaya143/Donate2Dine.git
   cd Donate2Dine
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Django:**
   ```bash
   pip install django==3.2.25
   ```

4. **Apply Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   > Navigate to `http://127.0.0.1:8000` in your web browser.

### Creating an Admin (Superuser)
To access the admin panel at `http://127.0.0.1:8000/admin`:
```bash
python manage.py createsuperuser
```

---

## 📸 Platform Previews

- **Rich Authentication UI**: Choose your role distinctly before joining the platform.
- **Interactive Dashboards**: See your active listings or active claims instantly upon login.
- **Real-time Feel Chat**: Communicate seamlessly inside a native messaging interface.

*(Screenshots can be added here)*

---

*Made with ❤️ to combat food waste and feed communities.*
