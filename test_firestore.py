from firebase_config import db

# Test Firestore connection
def get_bookings():
    bookings_ref = db.collection("bookings")  # Replace 'bookings' with your collection name
    docs = bookings_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

if __name__ == "__main__":
    get_bookings()
