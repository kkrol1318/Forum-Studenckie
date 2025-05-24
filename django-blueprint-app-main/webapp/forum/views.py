from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'forum/index.html') 

def frequent_questions(request):
    return render(request,'forum/frequent_questions.html') 

# forum/views.py
from django.shortcuts       import render, redirect
from django.contrib.auth.decorators import login_required
from django.http            import HttpResponseForbidden
from .models                import KoloMembership, ForumPost
from .forms                 import ForumPostForm

@login_required
def join_kolo(request, kolo):
    if request.method == 'POST':
        KoloMembership.objects.get_or_create(user=request.user, kolo=kolo)
        return redirect('forum:forum', kolo=kolo)
    return HttpResponseForbidden("Invalid request")

@login_required
def forum_view(request, kolo):
    # Check membership
    if not KoloMembership.objects.filter(user=request.user, kolo=kolo).exists():
        return redirect('main:kolo'+kolo.split('-')[1])

    posts = ForumPost.objects.filter(kolo=kolo).order_by('-created_at')

    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.kolo   = kolo
            post.save()
            return redirect('forum:forum', kolo=kolo)
    else:
        form = ForumPostForm()

    return render(request, 'forum/forum.html', {
        'kolo':  kolo,
        'form':  form,
        'posts': posts,
    })
