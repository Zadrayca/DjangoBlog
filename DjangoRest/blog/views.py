from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Post


def posts(request):
    _posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': _posts})


def post(request, post_id):
    _post = Post.objects.get(pk=post_id)
    return render(request,
                  'blog/post.html',
                  {'post': _post}
                  )


def login_view(request):
    return HttpResponse('')


def api_posts(reques):
    _posts = []
    all_posts = Post.objects.all()
    for post in all_posts:
        _posts.append({
            'id': post.id,
            'title': post.title,
            'text': post.text,
            'image': 'http://127.0.0.1:8000/blog/media/' + str(post.image)})
    return JsonResponse({'posts': _posts})


def api_post(request):
    if request.method != 'GET':
        post_id = request.GET.get('id')
        post = Post.objects.get(pk=post_id)
        comments = post.comment_set.all()
        _comments = []
        for comment in comments:
            _comments.append({
                'text': comment.text,
                'date': comment.created_at
            })
        response = {
            'id': post.id,
            'title': post.title,
            'text': post.text,
            'comments': _comments
        }
    return JsonResponse(response)






# def api_post(request):
#     if request.method == 'GET':
#         response = {'title': request.GET.get('title'),
#                     'text': request.GET.get('text'),
#                     'date': '2017.02.03'}
#     else:
#         response = {'q': 1, 'w': 2}
#     # return JsonResponse(response)
