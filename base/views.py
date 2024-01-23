from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        token['emaillllll'] = user.email
        token['age'] = "12"
        # ...


        return token




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

































# Create your views here.
from django.http import JsonResponse

from base.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


@api_view(['GET'])
def index(req,id=-1):
    temp_books=Book.objects.get(id=id)
    return Response("index")
    return Response (BookSerializer(temp_books,many=False).data)



def about(req):
    return Response('Hello Worldddddd', safe=False)


@api_view(['GET','POST','DELETE','PUT'])
def books(req,id=-1):
    if req.method =='GET':
        if id > -1:
            temp_books=Book.objects.get(id=id)
            return Response (BookSerializer(temp_books,many=False).data)
        all_tasks=BookSerializer(Book.objects.all(),many=True).data
        return Response ( all_tasks)

    if req.method =='POST':
        tsk_serializer = BookSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post done")
      
    if req.method =='DELETE':
        try:
            temp_books=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")    
       
        temp_books.delete()
        return Response ("Delete done")
    

    if req.method =='PUT':
        try:
            temp_books=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")
       
        ser = BookSerializer(data=req.data)
        old_task = Book.objects.get(id=id)
        res = ser.update(old_task, req.data)
        return Response("upd done")
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])    
def secret(req):
    return Response('secret')









    





    


   
