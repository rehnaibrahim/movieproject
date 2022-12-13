from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie5
from . forms import MovieForm

# Create your views here.


def index(request):
    movie=movie5.objects.all()
    context={
        'movie_list':movie
    }

    return render(request,'index.html',context)


def detail(request, movie_id):
    movie=movie5.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie':movie})


def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']

        movie=movie5(name=name,desc=desc,year=year,img=img)

        movie.save()

    return render(request,'add.html')


def update(request,id):
    movie=movie5.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=="POST":
        movie=movie5.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

