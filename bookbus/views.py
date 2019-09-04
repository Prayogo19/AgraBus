from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'Penyewaan Bus',
		'heading':'Penyewaan Bus Pariwisata Agra Mas'
	}
	return render(request, 'bookbus/index.html', context)