from django.shortcuts import render
from movieapp.forms import AbtMovieForm
from movieapp.models import AbtMovie
# Create your views here.

def Home_View(request):
    return render(request,'movieapp/Home.html')

def Movie_list_view(request):
    Add_Movie = AbtMovie.objects.all()
    print(Add_Movie)
    return render(request,'movieapp/MovieList.html',{'Add_Movie':Add_Movie})

def Add_Movie_view(request):
    form = AbtMovieForm()
    if request.method=='POST':
        form =AbtMovieForm(request.POST)
    if form.is_valid():
        form.save()
        print('success')
    return render(request,'movieapp/AddMovie.html',{'form':form})
