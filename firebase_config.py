import firebase_admin
from firebase_admin import credentials, firestore

# Path to the downloaded service account key JSON file
SERVICE_ACCOUNT_KEY_PATH = "firebase-account-key.json"

# Initialize Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()
