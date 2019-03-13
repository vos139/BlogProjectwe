from django.urls import path, include
from . import views
#from django.urls import reverse_lazy
#from django.contrib.auth import views as auth_views
#from django.conf import settings

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('learner/', include(([
        path('',views.learn_post_list, name='learn_post_list'),
        path('post/<int:pk>/', views.learn_post_detail, name='learn_post_detail'),
        path('post/new', views.learn_post_new, name='learn_post_new'),
        path('post/<int:pk>/edit/', views.learn_post_edit, name='learn_post_edit'),
        path('post/<int:pk>/view/', views.view_learn, name='view_learn'),
        path('post/<int:pk>/reply/', views.learn_add_reply, name='learn_add_reply'),
        ]))),
    path('consultant/', include(([
        path('', views.post_list, name='post_list'),
        path('post/<int:pk>/', views.post_detail, name='post_detail'),
        path('post/new', views.post_new, name='post_new'),
        path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
        path('post/<int:pk>/reply', views.add_reply, name='add_reply'),
        path('post/<int:pk>/view', views.view_reply, name='view_reply'),
        ]))),
    path('links', views.links, name='usefull_links'),
    ]
