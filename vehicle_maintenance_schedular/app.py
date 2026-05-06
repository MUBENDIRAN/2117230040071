from fastapi import FastAPI
import os
import requests
from dotenv import load_dotenv
import sys
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__),"..")
    )
)
from logging_middleware.logger import log


load_dotenv()

TOKEN=os.getenv("ACCESS_TOKEN")

HEADERS={
    "Authorization":f"Bearer{TOKEN}"
}

DEPOT_URL="http://20.244.56.144/evaluation-service/depots"
VEHICLE_URL="http://20.244.56.144/evaluation-service/vehicles"

app = FastAPI()

@app.get("/schedule")
def schedule():
    try:
        log(
            "backend",
            "info",
            "service",
            "Fetching depots"
        )

        depot_response=requests.get(
            DEPOT_URL,
            headers=HEADERS
        )

        vehicle_response=requests.get(
            VEHICLE_URL,
            headers=HEADERS
        )

        depots=depot_response.json()["deposts"]
        vehicles=vehicle_response.json()["vehicles"]
        mechanic_hours=depots[0]["mechanicHours"]

        log(
            "backend",
            "info",
            "service",
            f"Mechanic hours: {mechanic_hours}"
        )

        n=len(vehicles)
        
        dp=[[0]*(mechanic_hours+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            duration=vehicles[i-1]["Duration"]
            impact=vehicles[i-1]["Impact"]

            for j in range(mechanic_hours+1):
                if duration<=j:
                    dp[i][j]=max(
                        impact+dp[i-1][j-duration],
                        dp[i-1][j]
                    )

                else:
                    dp[i][j]=dp[i-1][j]

        max_impact=dp[n][mechanic_hours]

        log(
            "backend",
            "info",
            "service",
            "Scheduling completed successfully"
        )

        return{
        "mechanicHours": mechanic_hours,
        "maxImpact": max_impact   
        }

    except Exception as e:
        log(
            "backend",
            "error",
            "handler",
            str(e)
        )

        return {"error":str(e)} 