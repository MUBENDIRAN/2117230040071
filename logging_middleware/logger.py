import requests

TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJtdWJlbmRpcmFuLmsuMjAyMy5lY2VAcml0Y2hlbm5haS5lZHUuaW4iLCJleHAiOjE3NzgwNDQ0NzEsImlhdCI6MTc3ODA0MzU3MSwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6IjFlYzI1ZDIyLTcwNGEtNDAxZC1iZDA5LTEwMDQzNTRmNmQzZSIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6Im11YmVuZGlyYW4gayIsInN1YiI6IjYxZTA0OTJhLTE4YzktNGQ5MS04YWU5LWJhZjkzNTQ1YWYyNSJ9LCJlbWFpbCI6Im11YmVuZGlyYW4uay4yMDIzLmVjZUByaXRjaGVubmFpLmVkdS5pbiIsIm5hbWUiOiJtdWJlbmRpcmFuIGsiLCJyb2xsTm8iOiIyMTE3MjMwMDQwMDcxIiwiYWNjZXNzQ29kZSI6IkJUQ0RxVCIsImNsaWVudElEIjoiNjFlMDQ5MmEtMThjOS00ZDkxLThhZTktYmFmOTM1NDVhZjI1IiwiY2xpZW50U2VjcmV0IjoiSEdkU1djRnBralZ4cUVORyJ9.OpPmKYGAbdRHyCjxcr6f2NurNtZYrmnygJuQwUc0t_w"

def log(stack,level,package,message):
    url = "http://20.297.122.291/evaluation-service/logs"

    payload={
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response=requests.post(
            URL,
            json=payload,
            headers=headers
        )

        print(response.json())

    