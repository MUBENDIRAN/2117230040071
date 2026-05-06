import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN=os.getenv("ACCESS_TOKEN")

def log(stack,level,package,message):
    url = "https://20.244.56.144/evaluation-service/logs"

    payload={
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response=requests.post(
            url,
            json=payload,
            headers=headers
        )

        print(response.json())

    except Exception as e:
        print("Logging failed:",e)


log(
    "backend",
    "info",
    "middleware",
    "Logger test successful"
)