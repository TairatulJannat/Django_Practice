from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
from django.db.models import Avg

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1': 'This is a list of Musicians','musician_list':musician_list,'sample_text':"sample text"}
    return render(request, 'first_app/index.html', context=diction)

def contact(request):
    return HttpResponse("<h1>I am the contact page</h1>")

# def form(request):
#     new_form = forms.user_form()
#     new_musician_form = forms.MusicianForm()
#
#     diction = {
#         'test_form': new_form,
#         'musician_form': new_musician_form,
#         'heading_1': "This form is created using Django library",
#     }
#
#     if request.method == "POST":
#         new_form = forms.user_form(request.POST)
#         new_musician_form = forms.MusicianForm(request.POST)
#
#         # Handle user_form
#         if new_form.is_valid():
#             user_name = new_form.cleaned_data['user_name']
#             user_dob = new_form.cleaned_data['user_dob']
#             user_email = new_form.cleaned_data['user_email']
#
#             diction.update({
#                 'user_name': user_name,
#                 'user_dob': user_dob,
#                 'user_email': f"{user_email} - field match!!",
#                 'boolean_field': new_form.cleaned_data['boolean_field'],
#                 'field': new_form.cleaned_data['field'],
#                 'choice': new_form.cleaned_data['choice'],
#                 'form_submitted': "yes",
#             })
#
#         # Handle MusicianForm
#         if new_musician_form.is_valid():
#             new_musician_form.save(commit=True)
#             return redirect('index')  # Proper HTTP redirect to the index view
#
#     # Pass both forms to the template
#     diction['test_form'] = new_form
#     diction['musician_form'] = new_musician_form
#
#     return render(request, 'first_app/form.html', context=diction)


def album_list(request):
    diction = {'title':"List of Albums"}
    return render(request,'first_app/album_list.html',context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
     form = forms.MusicianForm(request.POST)
    if form.is_valid():
        form.save(commit= True)
        return index(request)

    diction = {'title':"Musician Form",'musician_form':form}
    return render(request,'first_app/musician_form.html',context=diction)
def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)

    diction = {'title':"Add Album",'album_form':form}
    return render(request,'first_app/album_form.html',context=diction)
def album_list(request, artist_id):
    artist_info= Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))


    diction = {'title': "List of Albums", 'artist_info':artist_info, 'album_list':album_list, 'artist_rating':artist_rating}
    return render(request, 'first_app/album_list.html', context= diction)

def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)
    diction= {'edit_form':form}
    return render(request,'first_app/edit_artist.html',context= diction)

def edit_album(request, album_id):
    album_info= Album.objects.get(pk=1)
    form = forms.AlbumForm(instance=album_info)
    diction = {}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated!'})
    diction.update({'edit_form':form})
    diction.update({'album_id':album_id})
    return render(request, 'first_app/edit_album.html',context = diction)
def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction ={'delete_success':'Deleted Successfully!'}
    return render(request, 'first_app/delete.html',context=diction)