from django.shortcuts import render
from .models import Post, User

# Create your views here.


def Home(request, user_id):

    user = User.objects.get(id=user_id)

    posts = Post.objects.filter(user=user) 
    return render(
        request,
        'instagram/home.html',
        {'posts': posts}
    )
