from hood.models import Post, Profile, Neighbourhood
from django.contrib.auth.models import User
from hood.forms import NewHoodForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    # return HttpResponse('Hi there')
    hoods = Neighbourhood.objects.all()
    return render(request, 'index.html', {"hoods": hoods})


def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user.id).all
    return render(request, 'registration/profile.html', {"posts": posts})


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    obj = get_object_or_404(Profile, user_id=id)
    obj2 = get_object_or_404(User, id=id)
    form = UpdateProfileForm(request.POST or None, request.FILES, instance=obj)
    form2 = UpdateUserForm(request.POST or None, instance=obj2)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return HttpResponseRedirect("/profile")

    return render(request, "registration/update_profile.html", {"form": form, "form2": form2})


@login_required(login_url='/accounts/login/')
def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('index')


@login_required(login_url='/accounts/login')
def view_hood(request, id):
    hood = Neighbourhood.objects.get(id=id)
    current_user = request.user
    return render(request, 'view_hood.html',  {
        'hood': hood,
    })
