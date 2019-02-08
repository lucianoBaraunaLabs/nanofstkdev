# -*- coding: utf-8 -*-
from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = ""
# Seu Auth Token, encontre em twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+", 
    from_="+",
    body="Olá me chamo Luciano Baraúna e estou testendo meu aprendizados..."
)

print(message.sid)
