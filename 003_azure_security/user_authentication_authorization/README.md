## User authentication and authorization

### General information

The Microsoft identity platform helps you build applications your users and customers can sign in to using their Microsoft identities or social accounts, and provide authorized access to your own APIs or Microsoft APIs like Microsoft Graph.

There are several components that make up the Microsoft identity platform:

- _OAuth 2.0 and OpenID Connect standard-compliant authentication service_.
- _Open-source libraries_.
- _Microsoft identity platform endpoint_.
- _Application management portal_.
- _Application configuration API and PowerShell_.

---

### Service principals

When you register an app in the Azure portal, you choose whether it is:

- **Single tenant**: only accessible in your tenant
- **Multi-tenant**: accessible in other tenants

There are three types of service principal:

- **Application**.
- **Managed identity**.
- **Legacy**.

The application object is the _global_ representation of your application for use across all tenants, and the service principal is the _local_ representation for use in a specific tenant. The application object serves as the template from which common and default properties are _derived_ for use in creating corresponding service principal objects.

---

### Permissions and consent

The Microsoft identity platform supports two types of permissions: _delegated access_ and _app-only access_.

- **Delegated access** are used by apps that have a signed-in user present. For these apps, either the user or an administrator consents to the permissions that the app requests. The app is delegated with the permission to act as a signed-in user when it makes calls to the target resource.
- **App-only access permissions** are used by apps that run without a signed-in user present, for example, apps that run as background services or daemons. Only an administrator can consent to app-only access permissions.

---

### Consent types

- **Static user consent**.
- **Incremental and dynamic user consent**.
- **Admin consent**.

---

### Key Components\*

| Component                   | Description                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| App Registration            | Registers your app with Microsoft Entra ID                              |
| Client ID                   | Unique ID of the app                                                    |
| Tenant ID                   | ID of your Azure AD tenant                                              |
| Client Secret / Certificate | Credential for confidential apps                                        |
| Redirect URI                | Where the identity platform sends tokens after authentication           |
| Scopes                      | Define permissions (e.g.: `User.Read`, `api://<app-id>/access_as_user`) |

---

## Authentication by using the Microsoft Authentication Library (MSAL)

### Authentication flows

![user-aa-1](../user_authentication_authorization/images/user-aa-1.png)

### Authentication implementation using Python SDK

1. Code snippet:

```python
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
```

2. Execution:

![user-aa-2](../user_authentication_authorization/images/user-aa-2.png)

![user-aa-3](../user_authentication_authorization/images/user-aa-3.png)

---
