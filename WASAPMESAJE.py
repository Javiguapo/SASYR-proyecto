from twilio.rest import Client

account_sid = 'AC0f69baa2d651c4592d2832192c324e24'
auth_token = 'a5af18c6984ae15e06604c492db72b9c'
twilio_client = Client(account_sid, auth_token)

message = twilio_client.messages.create(
body='Autoridades en camino - Situación de riesgo CRITICA detectada.  Ubicacion:Carr. Cdad. Sahagún-Pachuca Km. 20, Ex-Hacienda de Santa Bárbara, 43830 Zempoala, Hgo.',
from_='whatsapp:+14155238886',  # Reemplaza esto con tu número de WhatsApp de Twilio
to='whatsapp:+5217717209208'  # Reemplaza esto con el número al que deseas enviar el mensaje
)
print(message.sid)  # Puedes imprimir el SID del mensaje para verificar si se ha enviado correctamente

message = twilio_client.messages.create(
body='Autoridades en camino - Situación de riesgo CRITICA detectada.  Ubicacion:Carr. Cdad. Sahagún-Pachuca Km. 20, Ex-Hacienda de Santa Bárbara, 43830 Zempoala, Hgo.',
from_='whatsapp:+14155238886',  # Reemplaza esto con tu número de WhatsApp de Twilio
to='whatsapp:+5217791126726'  # Reemplaza esto con el número al que deseas enviar el mensaje
)
print(message.sid)  # Puedes imprimir el SID del mensaje para verificar si se ha enviado correctamente

message = twilio_client.messages.create(
body='Autoridades en camino - Situación de riesgo CRITICA detectada.  Ubicacion:Carr. Cdad. Sahagún-Pachuca Km. 20, Ex-Hacienda de Santa Bárbara, 43830 Zempoala, Hgo.',
from_='whatsapp:+14155238886',  # Reemplaza esto con tu número de WhatsApp de Twilio
to='whatsapp:+521771445084'  # Reemplaza esto con el número al que deseas enviar el mensaje
)
print(message.sid)  # Puedes imprimir el SID del mensaje para verificar si se ha enviado correctamente
message = twilio_client.messages.create(
  from_='+14154888981',
  body='Autoridades en camino - Situación de riesgo CRITICA detectada.  Ubicacion:Carr. Cdad. Sahagún-Pachuca Km. 20, Ex-Hacienda de Santa Bárbara, 43830 Zempoala, Hgo.',
  to='+527711445084'
)
message = twilio_client.messages.create(
  from_='+14154888981',
  body='Autoridades en camino - Situación de riesgo CRITICA detectada.  Ubicacion:Carr. Cdad. Sahagún-Pachuca Km. 20, Ex-Hacienda de Santa Bárbara, 43830 Zempoala, Hgo.',
  to='+527717209208'
)

