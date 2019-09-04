from django.shortcuts import render

def index(request):
	context = {
	'title':'Agra Mas',

	}
	return render(request, 'index.html', context)

def error(request,input):
	context = {
	'hal':input,
	}
	return render(request, 'error.html',context)

def error2(request,input):
	context = {
	'hal':input,
	}
	return render(request, 'error.html',context)