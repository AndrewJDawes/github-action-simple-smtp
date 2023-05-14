import sys
import smtplib

host = sys.argv[1]
port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
sender = sys.argv[5]
recipient = sys.argv[6]
subject = sys.argv[7]
body = sys.argv[8]

# Set up SMTP connection
server = smtplib.SMTP(host, port)
server.starttls()
server.login(username, password)

# Compose message
message = f'Subject: {subject}\n\n{body}'

# Send email
server.sendmail(sender, recipient, message)

# Close SMTP connection
server.quit()
