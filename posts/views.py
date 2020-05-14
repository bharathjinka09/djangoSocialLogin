from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator

from .models import Post
from .forms import PostForm

# Create your views here.


def not_logged_in(request):
	return render(request, 'not_logged_in.html')

@login_required(login_url='/not_logged_in')
def home(request):
	user = request.user
	if request.user.is_authenticated:
		posts_list = Post.objects.filter(author=user).order_by('-timestamp')
	else:
		posts_list = Post.objects.all()[::-1]
	print(posts_list)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts': posts, 'user':user}

	return render(request, 'home.html', context=context)


@login_required(login_url='/not_logged_in')
def create(request):

	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, 'Post Created')
			form = PostForm()

			return redirect('/')
	else:
		form = PostForm()

	context = {'form': form}
	return render(request, 'create.html', context)

# view single post
@login_required(login_url='/not_logged_in')
def post(request, id):
	posts = get_object_or_404(Post, id=id)
	context = {
		'id': id, 
		'title':posts.title, 
		'description': posts.description
		}
	return render(request, 'post.html', context)

@login_required(login_url='/not_logged_in')
def delete_post(request, id):
	obj = get_object_or_404(Post, id=id)
	# POST request
	if request.method == 'POST':
		obj.delete()
		messages.success(request, 'Post Deleted')
		return redirect('/')
	context = {
		'object':obj
	}
	return render(request, 'delete_post.html', context)

@method_decorator(login_required, name='dispatch')
class UpdatePostView(SuccessMessageMixin, UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'update_post.html'
	success_message = "Post updated successfully"