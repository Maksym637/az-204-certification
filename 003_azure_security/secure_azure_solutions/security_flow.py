import os

from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


load_dotenv("env/.secrets.env")

KEY_VAULT_URL = f"https://{os.getenv('KEY_VAULT_NAME')}.vault.azure.net"


def execute_security_flow():
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)

    while True:
        print(
            f"\n{'-' * 30}"
            "\nPlease select an option:"
            "\n 1. Create a new secret"
            "\n 2. List all secrets"
            "\n Type 'quit' to exit"
            f"\n{'-' * 30}"
        )

        choice = input("Enter your choice: ").strip().lower()

        match choice:
            case "1":
                create_secret(client)
            case "2":
                list_secrets(client)
            case "quit":
                break
            case _:
                print("Invalid option. Please enter 1, 2, or 'quit'.")


def create_secret(client: SecretClient):
    secret_name = input("Enter secret name: ").strip()
    secret_value = input("Enter secret value: ").strip()

    if not secret_name or not secret_value:
        print("Secret name and value cannot be empty.")
        return

    client.set_secret(name=secret_name, value=secret_value)
    print(f"Secret '{secret_name}' created successfully.")


def list_secrets(client: SecretClient):
    print("Listing all secrets in the vault:")

    for secret_prop in client.list_properties_of_secrets():
        secret = client.get_secret(secret_prop.name)
        print(f"\nName: {secret.name} \nValue: {secret.value}")


if __name__ == "__main__":
    execute_security_flow()
