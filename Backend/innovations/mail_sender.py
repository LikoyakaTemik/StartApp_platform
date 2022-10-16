import random
import smtplib, ssl



def sender(receiver):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "likoydes@gmail.com"
    receiver_email = receiver
    password = "alaeacjrnnqowboa"
    message = ""
    for i in range(0, 6):
        ch = random.randint(1, 10)
        message = message + str(ch)
    if(len(message) > 6):
        message = message[0] + message[1] + message[2] + message[3] + message[4] + message[5]
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
    return message
print(sender("bukanov.artem@mail.ru"))
