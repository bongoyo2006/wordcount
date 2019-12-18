from django.http import HttpResponse
from django.shortcuts import render

def print(request):
	return render(request,'home.html')