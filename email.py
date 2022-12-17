from mailjet_rest import Client
import os
api_key = '8114d1c532d2a3aff3f069b945434bc7'
api_secret = 'a44cb453fee56adb701abf3394c75b52'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "sivasankarstorage@gmail.com",
        "Name": "Sivasankar"
      },
      "To": [
        {
          "Email": "sivasankar53662@gmail.com",
          "Name": "Sivasankar"
        }
      ],
      "Subject": "Mytest passed",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())