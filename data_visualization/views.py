from django.shortcuts import render
from django.http import JsonResponse
import os
import time

def index(request):
	return render(request, 'data_visualization/index.html')

def reddit(request):
	return render(request, 'data_visualization/reddit.html')

def catch(request, basename):
	return render(request, 'data_visualization/unused/' + basename)


def test(request):
	# return render(request, 'data_visualization/unused/charts-area-line-boundaries.html')
	lst = []
	unused_dir_relative = 'templates/data_visualization/unused'
	lst = os.listdir(unused_dir_relative)
	for i in range(0,len(lst)-1):
		time.sleep(3)
		render(request, 'data_visualization/unused/' + lst[i])
	return(request, )