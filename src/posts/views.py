from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
# Create your views here.
from .forms import PostForm

def post_list(request):
    queryset = Post.objects.all()
    context ={
        'queryset': queryset
    }
    return render(request, 'posts/home.html', context)



def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context ={
        'query': instance
    }
    return render(request, 'posts/post_detail.html', context)



def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'posts/post_create.html', context)

    



def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        'query': instance,
        'form': form
    }
    return render(request, 'posts/post_create.html', context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect('posts:post-list')




