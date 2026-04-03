import requests

API_KEY = "sk-saksham-local-123"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

res = requests.get(
    "http://localhost:3001/api/v1/models",
    headers=headers
)

print(res.text)

print("Saksham Dubey")