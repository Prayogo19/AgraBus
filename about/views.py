from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'Tentang',
		'heading':'Tentang Sistem Informasi Penyewaan Bus Pariwisata Agra Mas'
	}

	return render(request, 'about/index.html', context)