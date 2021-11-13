import smtplib
import ssl


class Mail:
    def __init__(self, sender_email, sender_password):
        self.port = 465
        self.smtp_server_domain_name = 'smtp.gmail.com'
        self.sender_mail = sender_email
        self.password = sender_password

    def send(self, emails, email_subject, email_content):
        try:
            ssl_context = ssl.create_default_context()
            service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
            service.login(self.sender_mail, self.password)
            print('logged in ')

            for email in emails:
                result = service.sendmail(self.sender_mail, email, f"Subject: {email_subject} \n\n {email_content}")
                print('email sent')

            service.quit()
        except smtplib.SMTPAuthenticationError:
            print('could not sign into gmail')
