from cal_setup import setup_calendar
import datetime

def main():
   service = setup_calendar()
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   print("Getting the upcoming 10 events")
   events_result = (
        service.events().list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        ).execute()
    )
   events = events_result.get("items", [])

   if not events:
       print('No upcoming events found.')
   for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
       print(f"Time: {start}, Event name: {event['summary']}, Event ID: {event['id']}")

if __name__ == '__main__':
    main()