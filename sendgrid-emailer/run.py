import base64
import os
import sys

import sendgrid

API_KEY = os.environ["SENDGRID_API_KEY"]
FROM_EMAIL = os.environ["FROM_EMAIL"]
TO_EMAIL = os.environ["TO_EMAIL"]
OUTBOX = "/app/outbox"

CLIENT = sendgrid.SendGridAPIClient(api_key=API_KEY)

# Get each file in `/app/outbox`
attachments = []
for root, _, files in os.walk(OUTBOX):
    for name in files:
        file_path = os.path.join(root, name)
        with open(file_path, "rb") as f:
            raw_bytes = f.read()
            encoded_bytes = base64.b64encode(raw_bytes)
            attachments.append({"content": encoded_bytes.decode(), "filename": name})

data = {
    "personalizations": [
        {
          "to": [{"email": TO_EMAIL}],
          "subject": "Kindle email delivery"
        }
    ],
    "from": {
        "email": FROM_EMAIL
    },
    "attachments": attachments,
    "content": [
        {
            "type": "text/plain",
            "value": "I exist for the benefit of the sendgrid api!"
        }
    ]
}

try:
    response = CLIENT.client.mail.send.post(request_body=data)
except Exception as e:
    print(e)
    sys.exit(1)

print(response.status_code)
print(response.body)
print(response.headers)
