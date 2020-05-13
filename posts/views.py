from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm

# Create your views here.


def not_logged_in(request):
    return render(request, 'not_logged_in.html')


def home(request):
    posts_list = Post.objects.all()[::-1]

    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}

    return render(request, 'home.html', context=context)


@login_required(login_url='/not_logged_in')
def create(request):

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Created')
            form = PostForm()

            return redirect('/')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'create.html', context)
