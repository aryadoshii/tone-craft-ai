"""Raw HTTP probe using stdlib only — run with: python test_api.py"""
import json
import os
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("QUBRID_API_KEY")
BASE = "https://platform.qubrid.com"

def probe(method, path, body=None):
    url = BASE + path
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            text = resp.read().decode()[:300]
            print(f"  {method} {path} → {resp.status}: {text}")
    except urllib.error.HTTPError as e:
        body_text = e.read().decode()[:300]
        print(f"  {method} {path} → {e.code}: {body_text}")
    except Exception as e:
        print(f"  {method} {path} → ERROR: {e}")

payload = {
    "model": "zai-org/GLM-5",
    "messages": [{"role": "user", "content": "Say hello."}],
    "max_tokens": 50,
    "temperature": 0.7,
    "top_p": 1,
    "stream": False,
    "enable_thinking": False,
}

print("=== Testing GLM-5 ===")
probe("POST", "/v1/chat/completions", payload)
