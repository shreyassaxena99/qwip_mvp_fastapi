import pyqrcode
import hashlib
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase_config import db
from datetime import datetime

app = FastAPI()

# Secret key for generating secure HMAC signatures
SECRET_KEY = "super_secret_key"  # Replace with a strong, secret key!


# Define request model
class QRCodeRequest(BaseModel):
    booking_id: str
    pod_id: str
    user_id: str
    start_time: str
    end_time: str


# Generate a secure HMAC signature
def generate_signature(data: dict) -> str:
    serialized_data = json.dumps(data, sort_keys=True)
    return hashlib.sha256((serialized_data + SECRET_KEY).encode()).hexdigest()


@app.post("/generate_qr_code")
async def generate_qr_code(booking_id: str):
    try:
        # Fetch the booking document from Firestore
        booking_ref = db.collection("bookings").document(booking_id)
        booking_doc = booking_ref.get()

        if not booking_doc.exists:
            raise HTTPException(status_code=404, detail="Booking not found")

        # Retrieve booking details
        booking_data = booking_doc.to_dict()
        pod_id = booking_data.get("pod_id")
        user_id = booking_data.get("user_id")
        start_time = booking_data.get("start_time")  # Should be in ISO8601 format
        end_time = booking_data.get("end_time")  # Should be in ISO8601 format

        # Validate the necessary fields
        if not all([pod_id, user_id, start_time, end_time]):
            raise HTTPException(
                status_code=400,
                detail="Missing required booking information (pod_id, user_id, start_time, end_time)",
            )

        # Convert Firestore Timestamp to ISO8601 string
        if isinstance(start_time, datetime):
            start_time = start_time.isoformat()
        if isinstance(end_time, datetime):
            end_time = end_time.isoformat()


        # Prepare data for the QR code
        qr_data = {
            "booking_id": booking_id,
            "pod_id": pod_id,
            "user_id": user_id,
            "start_time": start_time,
            "end_time": end_time,
        }

        # Add a signature to prevent tampering
        qr_data["signature"] = generate_signature(qr_data)

        # Generate the QR code as a string
        qr_code = pyqrcode.create(json.dumps(qr_data))

        # Optionally, generate a Base64 image of the QR code
        qr_code_image = qr_code.png_as_base64_str(scale=5)

        # Update the booking document with QR code data
        booking_ref.update(
            {
                "qr_code_data": qr_data,  # Store encoded data
                "qr_code_image": qr_code_image,  # Store Base64 image (optional)
            }
        )

        return {"message": "QR code generated successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating QR code: {str(e)}"
        )
