# 🧹 Data Redundancy Removal System

This project is a simple web-based system that removes redundant data entries and prevents duplicate submissions using a Firebase Realtime Database and a Python Flask backend.

## 🚀 Features

- ✅ Classifies data as *redundant* or *unique* using validation.
- ✅ Prevents *duplicate data* from being stored.
- ✅ Stores *only unique* and verified entries in Firebase.
- ✅ Uses *Flask* for the backend, *HTML/CSS* for frontend UI.
- ✅ Makes the database efficient by *removing/avoiding redundancy*.

---

## 🛠️ Tech Stack

- *Python (Flask)* – Web framework
- *HTML & CSS* – Frontend
- *Firebase Realtime Database* – Cloud database
- *Firebase Admin SDK* – For authentication and database control

---

## ⚙️ Setup Instructions

1. *Clone the repository*

    git clone https://github.com/your-username/data-redundancy-removal.git
    cd data-redundancy-removal

2. Install dependencies

    pip install -r requirements.txt

3. Add your Firebase credentials

   Download your Firebase Admin SDK file from Firebase Console.
   Rename it to: firebase_config.json
   Place it in the root folder (same as app.py)

> 🔐 Never upload this file to anywhere

4. Run the Flask app

   python app.py

5. Open your browser and visit: http://127.0.0.1:5000


---

Disclaimer

  This project is for educational purposes. Ensure you do not expose private keys or credentials when sharing or deploying this project publicly.


---

👩‍💻 Author

Vendra Naveena
Intern @ CodeAlpha
GitHub: navi-navi-612
