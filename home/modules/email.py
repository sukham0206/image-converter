from django.core.mail import EmailMessage


def send_email(email_id, path):
    email = EmailMessage(
        'Hello',
        'Thank you for using this service',
        to=[email_id]
    )
    email.attach_file(path)
    email.send()