from django.urls import path
from BLog import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('post_1/', views.post_1, name='post_1'),
    path('post_2/', views.post_2, name='post_2'),
    path('post_3/', views.post_3, name='post_3'),
    path('post_4/', views.post_4, name='post_4'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
]
