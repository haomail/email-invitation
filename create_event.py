from cal_setup import setup_calendar
import datetime 

def main():
    service = setup_calendar()
    with open('emails.txt', 'r') as file:
        emails = [line.strip() for line in file]
    event = {
            "summary": "[HMTE] 3rd Meeting Divisi Akademik",
            "description": "Agenda: Pembuatan KAK",
            "colorId": "9",
            "start": {
                "dateTime": "2024-02-12T21:00:00+07:00",
                "timeZone": "Asia/Jakarta"
            },
            "end": {
                "dateTime": "2024-02-12T22:00:00+07:00",
                "timeZone": "Asia/Jakarta"
            },
            "attendees": [{"email": email} for email in emails],
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "popup", "minutes":10}
                ]
            },
            #"location": "Toko Kopi Seduh",
            "conferenceData": {"createRequest": {"conferenceSolutionKey": {"type": "hangoutsMeet"},"requestId": "3rd Meeting Divisi Akademik"}},
        }
    event = service.events().insert(calendarId="primary",body=event,sendNotifications=True,conferenceDataVersion=1).execute()

    print(f"Event created at {event.get('htmlLink')}")
    print("Created event")
    print("id: ", event['id'])
    print("summary: ", event['summary'])
    print("starts at: ", event['start']['dateTime'])
    print("ends at: ", event['end']['dateTime'])

if __name__ == "__main__":
  main()

"""
event = {
        "summary": "Create Event Using Google Calendar API",
        "description": "Broadcast Messages",
        "colorId": "9",
        "start": {
            "dateTime": "2024-02-03T10:00:00+07:00",
            "timeZone": "Asia/Jakarta"
            },
        "end": {
            "dateTime": "2024-02-03T11:00:00+07:00",
            "timeZone": "Asia/Jakarta"
            },
        "attendees": [{"email": email} for email in emails],
        "reminders": {
            "useDefault": False,
            "overrides": [
                    {"method": "popup", "minutes":30}
                ]
            },
        "location": "Somewhere"
        #"conferenceData": {"createRequest": {"conferenceSolutionKey": {"type": "hangoutsMeet"},"requestId": "1st Meeting Divisi Akademik"}},
        }
    event = service.events().insert(calendarId="primary",body=event,sendNotifications=True).execute() */
    """