from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'homepage.html')
	# #This is just going make a message pop up that says "homepage"
	# return HttpResponse('homepage')

	# # This is us using the templates folder and plugging in the html when it's called upon
	# # Don't forget to add the template folder to the settings.py>Templates>Dirs portion or the template wont function properly
	# return render(request, 'homepage.html')

def about(request):
	return render(request, 'about.html')
	
	# #This is just going make a message pop up that says "about"
	# return HttpResponse('about')

	# # This is us using the templates folder and plugging in the html when it's called upon
	# # Don't forget to add the template folder to the settings.py>Templates>Dirs portion or the template wont function properly
	# return render(request, 'about.html')