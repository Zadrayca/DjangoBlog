from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^api/posts/$', views.api_post, name='api_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
