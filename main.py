from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(slack_name: str, track: str):

    now = datetime.utcnow()
    today = now.strftime('%A')
    now =now.replace(microsecond=0)

    response = {"slack_name": slack_name,
                "current_day": today,
                "utc_time": now,
                "track": track,
                "github_file_url": "https",
                "github_repo_url": "https://github.com/Ideeee/hngfirsttask",
                "status_code": 200
                }
    
    return response