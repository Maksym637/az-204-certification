import os

from dotenv import load_dotenv

import msal


load_dotenv("env/.secrets.env")

CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")


AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["User.Read"]


def acquire_token_interactively():
    app = msal.PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY)
    accounts = app.get_accounts()

    if accounts:
        result = app.acquire_token_silent(scopes=SCOPES, account=accounts[0])
    else:
        result = None

    if not result:
        result = app.acquire_token_interactive(scopes=SCOPES)

    return result


if __name__ == "__main__":
    token_response = acquire_token_interactively()
    access_token = token_response.get("access_token", None)

    if access_token:
        print(f"Access token: {access_token}")
    else:
        print("An error occurred while getting an access token")
