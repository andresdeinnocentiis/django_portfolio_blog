from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .serializers import ContactSerializer

@api_view(['POST'])
def send_email(request):

    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        
        # email sending logic:
        
        send_mail(
            subject=f"New message from {name} ({email})",
            message=f"This is a message from '{name}' ({email}): \n\n {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': serializer.errors})




