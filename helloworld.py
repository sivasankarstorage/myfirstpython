from twilio.rest import Client 
 
account_sid = 'ACd996fbf5777b9272b7366f8425dcf29b' 
auth_token = '[Redacted]'
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+919150207116' 
                          ) 
 
print(message.sid)
print('Hello World')