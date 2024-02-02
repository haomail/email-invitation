import os.path
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json")

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPES)
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

try:
    service = build("calendar", "v3", credentials=creds)
    event = {
        "summary": "[HMTE] 1st Meeting Divisi Akademik",
        "description": "Proker setahun kedepan",
        "colorId": "9",
        "start": {
            "dateTime": "2024-02-02T16:30:00+07:00",
            "timeZone": "Asia/Jakarta"
        },
        "end": {
            "dateTime": "2024-02-02T19:40:00+07:00",
            "timeZone": "Asia/Jakarta"
        },
        "attendees": [for email in emails.txt],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "popup", "minutes":10}
            ]
        },
        "conferenceData": {"createRequest": {"requestId": "1st Meeting Divisi Akademik", "conferenceSolutionKey": {"type": "hangoutsMeet"}}},
    }
    event = service.events().insert(calendarId="primary",body=event).execute()
    print(f"Event created {event.get('htmlLink')}")

except HttpError as error:
    print("An error occured!")