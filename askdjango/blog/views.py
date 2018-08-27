from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')    #request get 인자중에 q가 있으면 가져오고 없으면 빈것으로 가져온다.
    if q:
        qs = qs.filter(title__icontains = q)

    return render(request, 'blog/post_list.html',{
        'post_list': qs,
        'q': q,
    })
 

def post_detail(request, id):
#   try:
#      post= Post.objects.get(id=id)
#    except Post.deosNotExist:
#        raise Http404

    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html',{
        'post' : post,
    })
