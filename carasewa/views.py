from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title':'Cara Penyewaan',
		'heading':'Cara Penyewaan Bus Pariwisata Agra Mas'
	}

	return render(request, 'carasewa/index.html', context)