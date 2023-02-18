from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to my site!'
        html_message = render_to_string('../templates/components/welcome_email.html', {'user': instance})
        plain_message = strip_tags(html_message)
        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[instance.email],
        )
        
        email.attach_alternative(html_message, 'text/html')
        email.send()
        
        """
        send_mail(
            subject=subject,
            message=message,
            from_email=sender,
            recipient_list=[instance.email],
            fail_silently=False,
        )"""

        print("The EMAIL WAS SENT CARAJOOOO!!")