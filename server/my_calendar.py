import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# Set the path to your token JSON file
token_path = './token.json'

# Define the scopes for the Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def authenticate_and_get_service():
    creds = None

    # Load existing token from file if available
    if token_path:
        creds = Credentials.from_authorized_user_file(token_path)

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    # Build the Google Calendar API service
    service = build('calendar', 'v3', credentials=creds)

    return service

def get_latest_events(calendar_service, max_results=3):
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = calendar_service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=max_results,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    return events

def main():
    calendar_service = authenticate_and_get_service()
    latest_events = get_latest_events(calendar_service)

    if not latest_events:
        print('No upcoming events found.')
    else:
        print('Latest events:')
        for event in latest_events:
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            print(f"{event['summary']} ({start_time})")

if __name__ == '__main__':
    main()
