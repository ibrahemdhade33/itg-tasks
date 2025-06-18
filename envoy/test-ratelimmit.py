import requests
import time

DOMAIN = "https://test.local"
HEADERS = {"x-user-id": "one"}
NUM_REQUESTS = 15  # more than the 10 per minute limit
DELAY = 2  # delay between requests

for i in range(NUM_REQUESTS):
    try:
        response = requests.get(DOMAIN, headers=HEADERS, verify=False)
        print(f"[{i+1}] Status: {response.status_code}, Body: {response.text.strip()[:50]}")
    except Exception as e:
        print(f"[{i+1}] ❌ Error: {e}")
    time.sleep(DELAY)