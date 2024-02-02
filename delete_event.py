from cal_setup import setup_calendar
from googleapiclient import errors as googleapiclient_errors

def main():
    service = setup_calendar()
    try:
        service.events().delete(
            calendarId='primary',
            eventId='<ID event yang mau didelete>',
            ).execute()
    except googleapiclient_errors.HttpError:
        print("Failed to delete event")
    print(f"Event deleted")

if __name__ == '__main__':
    main()