import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK with the service account key
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Example: Add a document to a Firestore collection
doc_ref = db.collection('users').document('user1')
doc_ref.set({
    'name': 'John Doe',
    'email': 'johndoe@example.com'
})