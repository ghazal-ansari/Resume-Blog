from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('resume/', views.resume, name='Resume'),
    path('blog/', include('BLog.urls')),
]
