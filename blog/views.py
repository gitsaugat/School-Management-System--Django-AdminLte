from django.shortcuts import render, redirect
from .forms import AcademicPostCreationForm, GeneralPostCreationForm
from .models import Academic_Post, General_Post


def academic_posts(request):
    posts = Academic_Post.objects.all().order_by('-date_added')
    context = {
            'posts': posts
    }

    return render(request, 'blog/academic/posts.html', context)


def create_academic_post(request):
    if request.method == "POST":
        form = AcademicPostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                newPost = Academic_Post(
                    user=request.user,
                    image=form.cleaned_data['image'],
                    title=form.cleaned_data['title'],
                    content=form.cleaned_data['content']
                )
                try:
                    newPost.save()
                    return redirect('dashboard')
                except:
                    return redirect('404')
    form = AcademicPostCreationForm()
    context = {
        'form': form
    }

    return render(request, 'blog/academic/create.html', context)


def edit_academic_post(request, pk):
    post = Academic_Post.objects.filter(pk=pk).first()
    if request.method == "POST":
        if post:
            form = AcademicPostCreationForm(
                request.POST,
                request.FILES,
                instance=post
            )
            if form.is_valid():
                if request.user.is_authenticated:
                    if request.user == post.user:
                        post.image = form.cleaned_data['image']
                        post.title = form.cleaned_data['title']
                        post.content = form.cleaned_data['content']
                        try:
                            post.save()
                            return redirect('dashboard')
                        except:
                            return redirect('404')
    form = AcademicPostCreationForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'blog/academic/edit.html', context)


def delete_academic_post(request, pk):
    post = Academic_Post.objects.filter(pk=pk).first()
    if post:
        if request.method == "POST":
            if request.user.is_authenticated:
                if request.user == post.user:
                    try:
                        post.delete()
                        return redirect('dashboard')
                    except:
                        return redirect('404')


def general_posts(request):
    if request.method == "GET":
        posts = General_Post.objects.all().order_by('-date_added')
        context = {
            'posts': posts
        }

    return render(request, 'blog/general/posts.html', context)


def create_general_post(request):
    if request.method == "POST":
        form = GeneralPostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                newPost = General_Post(
                    user=request.user,
                    image=form.cleaned_data['image'],
                    title=form.cleaned_data['title'],
                    content=form.cleaned_data['content']
                )
                try:
                    newPost.save()
                    return redirect('dashboard')
                except:
                    return redirect('404')
    form = GeneralPostCreationForm()
    context = {
        'form': form
    }

    return render(request, 'blog/general/create.html', context)


def edit_general_post(request, pk):
    post = General_Post.objects.filter(pk=pk).first()
    if request.method == "POST":
        if post:
            form = GeneralPostCreationForm(
                request.POST,
                request.FILES,
                instance=post
            )
            if form.is_valid():
                if request.user.is_authenticated:
                    if request.user == post.user:
                        post.image = form.cleaned_data['image']
                        post.title = form.cleaned_data['title']
                        post.content = form.cleaned_data['content']
                        try:
                            post.save()
                            return redirect('dashboard')
                        except:
                            return redirect('404')
    form = GeneralPostCreationForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'blog/general/edit.html', context)


def delete_general_post(request, pk):
    post = General_Post.objects.filter(pk=pk).first()
    if post:
        if request.method == "POST":
            if request.user.is_authenticated:
                if request.user == post.user:
                    try:
                        post.delete()
                        return redirect('dashboard')
                    except:
                        return redirect('404')
    return render(request, 'blog/general/confirm.html')
