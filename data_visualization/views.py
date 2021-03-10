from django.shortcuts import render
from django.http import JsonResponse

def index(request):
	return render(request, 'data_visualization/index.html')

def reddit(request):
	return render(request, 'data_visualization/reddit.html')
