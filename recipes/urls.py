from django.urls import path

from recipes.views import contato, home, sobre

#  dominio/recipes/xxxx
urlpatterns = [
    path('', home), # Home
    path('sobre/', sobre), # sobre
    path('contato/', contato), # Contato
]
