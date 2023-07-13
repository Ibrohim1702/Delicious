from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('elements/', elements, name='elements'),
    path('contact/', contact, name='contact'),
    path('recipe/<int:pk>/', recipe, name='recipe'),
    path('category/<slug>/', category, name='category'),
    path('category/', category, name='category')
]