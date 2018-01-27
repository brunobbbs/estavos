import logging
import datetime
from dateutil import parser
from django.conf import settings
from googleapiclient import discovery
from google.oauth2 import service_account


class GApiCalendar:
    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        credentials = service_account.Credentials.from_service_account_file(
                settings.SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.calendar_id = 'vckp8teebn16mo8ak7g5l2m8v0@group.calendar.google.com'
        self.service = discovery.build('calendar', 'v3', credentials=credentials)

    def get_event(self, event_id):
        return self.service.events().get(calendarId=self.calendar_id, eventId=event_id).execute()

    def get_event_list(self, qtd=3):
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        eventsResult = self.service.events().list(
            calendarId=self.calendar_id,
            timeMin=now, maxResults=qtd, singleEvents=True,
            orderBy='startTime').execute().get('items', [])
        events = []
        for event in eventsResult:
            events.append(self.get_event(event.get('id')))
        return events

    def _parse_date(self, dt):
        dt = parser.parse(dt)
        time = dt.strftime('%H:%M')
        return {
            'datetime': dt,
            'time': time != '00:00' and time or '',
        }

    def get_upcoming_events(self, qtd=3):
        events = self.get_event_list()
        upcoming = []
        for event in events:
            dt = self._parse_date(event['start'].get('dateTime', event['start'].get('date')))
            upcoming.append({
                'datetime': dt['datetime'],
                'time': dt['time'],
                'location': event['location'],
                'summary': event['summary'],
            })
        return upcoming
