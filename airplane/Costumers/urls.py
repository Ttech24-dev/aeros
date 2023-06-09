from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('sign-up/', views.sign, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,    name='post_detail'),
    
] 