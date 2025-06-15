
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os

load_dotenv()

cred_path = os.getenv("FIREBASE_CRED_PATH")
db_url = os.getenv("FIREBASE_DB_URL")

# ✅ Ensure Firebase is initialized once
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("cred_path")
        firebase_admin.initialize_app(cred, {
            'databaseURL': db_url  # Replace this with your actual DB URL
        })

# Call init_firebase BEFORE any Firebase access
init_firebase()

# Get database reference
ref = db.reference('entries')

def is_duplicate_entry(email, description):
    existing_entries = ref.get()
    if existing_entries:
        for entry in existing_entries.values():
            if isinstance(entry, dict):
               if entry.get('email') == email and entry.get('description') == description:
                 return True
    return False

def is_unique_entry(email, description):
    return not is_duplicate_entry(email, description)

def save_to_firebase(name, email, description):
    my_dict = {
        'name': name,
        'email': email,
        'description': description
    }
    ref.push(my_dict)