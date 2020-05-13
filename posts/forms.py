from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
	title = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder':'Title'
		}
		))
	description = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control',
			'placeholder':'Description'
		}
		))
	class Meta:
		model = Post
		fields = ('title', 'description')
