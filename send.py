
from twilio.rest import Client

account_sid = 'sid'
auth_token = 'authtoken'
client = Client(account_sid, auth_token)
def send_message(update):
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hii, A new update has been made on ERP portal{}'.format(update),
    to='whatsapp:+917011678257'
    )

