from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from rest_framework import generics
from .serializers.serializer import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class UserInfo(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
	@api_view(['GET','POST'])
	def userList(request):
		if request.method == 'POST':
			serializer = UserSerializer(data= request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status = status.HTTP_201_CREATED)
			return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
	
	def unused(x):
		return x
	