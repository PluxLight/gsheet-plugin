# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import sys

# https://developers.google.com/sheets/api/quickstart/python
#  L JSON File

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def main(sheet_url, sheet_range, json_location, sheet_name):

    # spreadsheet ID
    SAMPLE_SPREADSHEET_ID = sheet_url.split('d/')[1]
    SAMPLE_SPREADSHEET_ID = SAMPLE_SPREADSHEET_ID.split('/')[0]

    # spreadsheet range
    SAMPLE_RANGE_NAME = sheet_name + '!' + sheet_range

    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                json_location, SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        sys.stdout.write('No data found,')
    else:
        for rows in values:
            for row in rows:
                sys.stdout.write(row + ',')
            sys.stdout.write('\n')

    # ex) print
    # a1,a2,a3
    # b1,b2,b3



if __name__ == '__main__':
    main()