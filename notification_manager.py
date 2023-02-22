from twilio.rest import Client
import smtplib

TWILIO_SID = "AC8141ae23b27acc198f336e6505c53be7"
TWILIO_AUTH_TOKEN = "eb2594f255a70a5659865d2939928ee3"
TWILIO_VIRTUAL_NUMBER = "+17472710343"
TWILIO_VERIFIED_NUMBER = "+917795744005"

MY_EMAIL = "dhyanRandomTest@gmail.com"
MY_PASSWORD = "bzogjcxihamvduxu"


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
