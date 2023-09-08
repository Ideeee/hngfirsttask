from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    response = "Welcome, please navigate to the /api route and add slack_name and track as query parameters"
    return response


@app.get("/api")
async def api(slack_name: str = "Idee", track: str = "Backend"):

    now = datetime.utcnow()
    today = now.strftime('%A')
    now =now.replace(microsecond=0)

    response = {"slack_name": slack_name,
                "current_day": today,
                "utc_time": now,
                "track": track,
                "github_file_url": "https://github.com/Ideeee/hngfirsttask/blob/main/main.py",
                "github_repo_url": "https://github.com/Ideeee/hngfirsttask",
                "status_code": 200
                }
    
    return response