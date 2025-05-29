# run_all.py

import subprocess

services = {
    "scraper": 8001,
    "indexer": 8002,
    "retriever": 8003,
    "llm_agent": 8004,
    "voice_agent": 8005,
}

for name, port in services.items():
    print(f"Starting {name} on port {port}...")
    subprocess.Popen(
        ["uvicorn", "main:app", "--port", str(port), "--reload"],
        cwd=f"./microservices/{name}"
    )
