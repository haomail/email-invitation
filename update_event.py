from datetime import datetime, timedelta
from cal_setup import setup_calendar


def main():
    service = setup_calendar()
    event_result = service.events().update(
        calendarId='primary',
        eventId='<Event ID yang mau diupdate>',
        body={
           "summary": 'Updated Automating calendar pt 2',
           "description": 'This is a tutorial example of automating google calendar with python, updated time.',
           "start": {"dateTime": "2024-02-03T10:00:00+07:00", "timeZone": 'Asia/Jakarta'},
           "end": {"dateTime": "2024-02-03T10:15:00+07:00", "timeZone": 'Asia/Jakarta'},
           },
        ).execute()

    print("Updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
    main()