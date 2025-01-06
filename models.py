from pydantic import BaseModel

class QRCodeRequest(BaseModel):
    booking_id: str
    pod_id: str
    user_id: str
    start_time: str  # ISO8601 formatted datetime (e.g., "2024-12-30T08:00:00")
    end_time: str    # ISO8601 formatted datetime
