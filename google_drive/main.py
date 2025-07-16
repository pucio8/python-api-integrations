import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# === Configuration ===
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CLIENT_SECRETS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json' # File to store the token after login

def authenticate_google():
    """
    Handles the Google Drive API authentication process.
    Returns valid credentials for API use.
    """
    creds = None
    # Check if the token file from a previous login exists.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh credentials if they are expired and a refresh token is available.
            creds.refresh(Request())
        else:
            # Create a flow object and run the local server for authorization.
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run.
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            
    return creds

def list_files(creds):
    """
    Uses the credentials to connect to the Drive API and lists 10 files.
    """
    try:
        # Build the service object to communicate with the Google Drive API.
        service = build('drive', 'v3', credentials=creds)
        print("\n📄 Fetching the 10 most recent files from your Google Drive...")
        
        # Call the Drive v3 API to list files.
        results = service.files().list(
            pageSize=10, 
            fields="files(id, name, webViewLink)",
            orderBy="modifiedTime desc" # Sort by most recently modified.
        ).execute()

        items = results.get('files', [])
        if not items:
            print("No files found.")
        else:
            print("Here are your recent files:")
            for item in items:
                print(f"- {item['name']} (ID: {item['id']})")
    
    except HttpError as error:
        print(f'An API error occurred: {error}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    
if __name__ == "__main__":
    print("🔄 Initializing connection with Google Drive...")
    credentials = authenticate_google()
    if credentials:
        list_files(credentials)
