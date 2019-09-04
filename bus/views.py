from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'Daftar Bus',
		'heading':'Daftar Bus Pariwisata Agra Mas'
	}

	return render(request, 'bus/index.html', context)