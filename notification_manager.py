from twilio.rest import Client
import smtplib
import os

TWILIO_SID = os.getenv("twillio_sid")
TWILIO_AUTH_TOKEN = os.getenv("twillio_auth_token")
TWILIO_VIRTUAL_NUMBER = os.getenv("twillio_virtual_no")
TWILIO_VERIFIED_NUMBER = os.getenv("twillio_verified_no")

MY_EMAIL = os.getenv("email")
MY_PASSWORD = os.getenv("google_app_password")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
