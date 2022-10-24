from django.urls import path

from recipes.views import home

#  dominio/recipes/xxxx
urlpatterns = [
    path('', home), # Home
]
