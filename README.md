# Qwip-MVP FastAPI Backend

This is the backend API for the **Qwip-MVP** project. It provides essential functionality for managing bookings, generating QR codes, and integrating with Firebase Firestore for real-time database management.

---

## Features

- **Generate QR Codes**:
  - Securely generate QR codes for bookings to unlock co-working pods.
  - Include tamper-proof signatures for validation.
- **Firestore Integration**:
  - Seamlessly interact with Firestore to retrieve and update booking data.
- **Scalable API**:
  - Built using FastAPI for high performance and scalability.

---

## Technologies Used

- **FastAPI**: For building the API endpoints.
- **Firebase Admin SDK**: For interacting with Firestore.
- **PyQRCode**: For generating QR codes.
- **pypng**: For rendering QR codes as PNG images.
- **Uvicorn**: For running the FastAPI application.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- Firebase project with Firestore configured
- A valid Firebase service account JSON file

### Steps

1. **Clone the Repository**:
   \`\`\`bash
   git clone https://github.com/shreyassaxena99/qwip_mvp_fastapi.git
   cd qwip_mvp_fastapi
   \`\`\`

2. **Create a Virtual Environment**:
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   \`\`\`

3. **Install Dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Setup Firebase**:
   - Place your Firebase service account JSON file in the root directory.
   - Rename it to \`firebase_service_account.json\` (or update the filename in the code).

5. **Run the Application**:
   \`\`\`bash
   uvicorn main:app --reload
   \`\`\`

   The API will be accessible at \`http://127.0.0.1:8000\`.

---

## API Endpoints

### **Generate QR Code**
Generate a QR code for a booking.

- **Endpoint**: `/generate_qr_code`
- **Method**: `GET`
- **Query Parameters**:
  - `booking_id` (string): The unique ID of the booking.
- **Response**:
  ```json
  {
    "message": "QR code generated successfully",
    "qr_code_data": {
      "booking_id": "booking123",
      "pod_id": "pod001",
      "user_id": "user123",
      "start_time": "2024-12-30T08:00:00",
      "end_time": "2024-12-30T09:00:00",
      "signature": "secure_signature"
    },
    "qr_code_image": "BASE64_ENCODED_IMAGE"
  }
  ```
- **Error Responses**:
  - `404`: If the booking is not found.
  - `500`: For any other internal server error.

---

## Project Structure

```
qwip_mvp_fastapi/
├── main.py                  # Entry point of the FastAPI application
├── firebase_config.py       # Firebase initialization and Firestore setup
├── requirements.txt         # Python dependencies
└── firebase_service_account.json # Firebase service account JSON (not in Git)
└── models.py                # Request Schema
└── test_firestore.py        # Testing file to check access to firestore
```

---

## Development Workflow

### Running Locally
1. Start the backend:
   ```bash
   uvicorn main:app --reload
   ```

2. Test the API with \`curl\` or any API client like Postman:
   ```bash
   curl "http://127.0.0.1:8000/generate_qr_code?booking_id=booking123"
   ```

---

## Adding New Features

### Example: Validate QR Code
1. Add a new endpoint in \`main.py\`:
   ```python
   @app.post("/validate_qr_code")
   async def validate_qr_code(data: dict):
       # Implement validation logic
       return {"message": "QR code validated successfully"}
   ```

2. Test the new endpoint locally before deploying.

---

## Deployment

### Local Deployment
Use `uvicorn` to run the app locally:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Production Deployment
Use a production server like **Gunicorn** with a process manager like **systemd** or containerize the app using Docker.

---

## Future Enhancements

1. **Authentication**:
   - Integrate Firebase Authentication to secure endpoints.
2. **Validation**:
   - Add a `/validate_qr_code` endpoint for QR code validation.
3. **Admin APIs**:
   - Add endpoints for managing pods and bookings.
4. **Error Logging**:
   - Use a logging framework to monitor errors and API usage.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push your branch and open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

**Author**: Shreyas Saxena  
**Email**: [your_email@example.com](mailto:your_email@example.com)  
**GitHub**: [shreyassaxena99](https://github.com/shreyassaxena99)