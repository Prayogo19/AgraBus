from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'Daftar Harga Bus',
		'heading':'Daftar Harga Penyewaan Bus Pariwisata Agra Mas'
	}

	return render(request, 'harga/index.html', context)