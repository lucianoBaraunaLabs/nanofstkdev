# -*- coding: utf-8 -*-
from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = "AC49229621f89b54eeb3aa6a9291d71059"
# Seu Auth Token, encontre em twilio.com/console
auth_token  = "d3fa2542f55073e07e13e2a3b0d1ee18"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521989314143", 
    from_="+5531933007061",
    body="Olá me chamo Luciano Baraúna e estou testendo meu aprendizados..."
)

print(message.sid)