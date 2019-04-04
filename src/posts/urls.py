from django.urls import path, include
#from .views import post_create, post_delete, post_detail, post_update, post_list
from .views import post_list, post_detail, post_create, post_update,post_delete


app_name = 'posts'


urlpatterns = [
    path('', post_list , name="post-list"),
    path('new/', post_create, name="post-create"),
    path('<id>/', post_detail, name="post-detail"),
    path('<id>/edit/', post_update, name="post-update"),
    path('<id>/delete/', post_delete, name="post-delete"),
]
