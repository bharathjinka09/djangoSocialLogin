from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.


def not_logged_in(request):
    return render(request, 'not_logged_in.html')


@login_required(login_url='/not_logged_in')
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context=context)
