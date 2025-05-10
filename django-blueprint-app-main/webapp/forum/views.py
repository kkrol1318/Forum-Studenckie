from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

#@login_required
def kolo_forum(request, kolo_slug):
    posts = Post.objects.filter(kolo=kolo_slug).order_by('-created_at')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.kolo = kolo_slug
            post.author = request.user
            post.save()
            return redirect('kolo_forum', kolo_slug=kolo_slug)
    else:
        form = PostForm()

    return render(request, 'forum/kolo_forum.html', {
        'posts': posts,
        'form': form,
        'kolo': kolo_slug
    })
