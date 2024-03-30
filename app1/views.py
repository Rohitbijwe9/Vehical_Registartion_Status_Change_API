from django.shortcuts import render
from .models import Registration
from .serializer import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail





class RegisterApiView(APIView):
    def get(self,request):
        reg=Registration.objects.all()
        serializer=RegistrationSerializer(reg,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            reg=serializer.save()
            uid=reg.user_id
            print('uid',uid)
            to_email=reg.user_email
            print('email',to_email)
            from_email = settings.EMAIL_HOST_USER
            subject = 'Applying For User Registration'
            message = f'You can check your Registartion status with this Registartion ID: {uid}'
            send_mail(subject, message, from_email, [to_email])
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"error": "Invalid data for user registration"}, status=status.HTTP_400_BAD_REQUEST)
    
class checkRegistrationstatus(APIView):
    def get(self,request,pk):
        try:
            reg=Registration.objects.get(user_id=pk)
            reg_status=reg.u_status
            return Response({'status':reg_status},status=status.HTTP_200_OK)
        except:
            return Response({'error':'registration not found'},status=status.HTTP_400_BAD_REQUEST)
        
    
class Approvereg(APIView):
    def get(self,request,pk):
        try:
            reg=Registration.objects.get(user_id=pk)
        except:
            return Response({'error':'registration not found'},status=status.HTTP_400_BAD_REQUEST)
        
        if reg.u_status=='pending':
            print(reg.u_status)
            reg.u_status='approved'
            reg.save()
            #for sending mail
            to_email=reg.user_email
            name=reg.user_name
            from_email = settings.EMAIL_HOST_USER
            subject = 'approved'
            message = f'congratulation {name} your vehical registration approved sucessfully...'
            send_mail(subject, message, from_email, [to_email])



            print(reg.u_status)
            return Response({'message':'register approved sucessfully'},status=status.HTTP_200_OK)
        else:
            return Response({"error": "registration is not in pending status"}, status=status.HTTP_400_BAD_REQUEST)




        







