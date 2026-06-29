from fastapi import APIRouter, Depends
from github import Github  # pip install PyGithub

router = APIRouter()

@router.get("/callback")
async def github_oauth_callback(code: str):
    # Exchange code for access token with GitHub
    token = exchange_code_for_token(code)
    g = Github(token)
    user = g.get_user()
    # Save user + token to DB, return JWT to frontend
    return {"username": user.login, "avatar": user.avatar_url}

@router.get("/activity/{username}")
async def get_activity(username: str, token: str):
    g = Github(token)
    user = g.get_user(username)
    events = []
    for event in user.get_events()[:20]:
        events.append({
            "type": event.type,       # PushEvent, PullRequestEvent, etc.
            "repo": event.repo.name,
            "created_at": str(event.created_at),
            "payload": event.payload
        })
    return events

@router.post("/webhook")
async def github_webhook(payload: dict):
    # GitHub sends this automatically on every push/PR
    # Parse and store as activity, link to tasks
    event_type = payload.get("action")
    # e.g. link commit message "#TASK-12" to that task
    return {"received": True}
