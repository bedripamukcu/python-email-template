import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import email.utils

def send(sender_email, sender_password, receiver_emails, subject, message, folder_path):
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

   
    msg = MIMEMultipart()
    msg['To'] = ', '.join(receiver_emails)
    msg['Subject'] = subject

    
    sender_name = 'Mail Message'
    sender_domain = 'YourDomain'
    msg['From'] = email.utils.formataddr((sender_name, sender_domain))

    html_message = f'''
        <html>
            <body>
                <h1>{subject}</h1>
                <p>{message}</p>
        '''

    
    image_id = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.png'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'rb') as file:
                image = MIMEImage(file.read())
                image.add_header('Content-ID', f'<{image_id}>')
                image.add_header('X-Attachment-Id', f'{image_id}')
                image.add_header('Content-Disposition', 'attachment', filename=file_name)
                msg.attach(image)
                html_message += f'<p><img src="cid:{image_id}" alt="{file_name}" /></p>'

    html_message += '''
            </body>
        </html>
    '''

    # Attach the HTML message to the email
    msg.attach(MIMEText(html_message, 'html', 'utf-8'))

    try:
        # Create a secure connection with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_emails, msg.as_string())

        # Close the connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))
