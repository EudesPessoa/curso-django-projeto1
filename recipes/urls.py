from django.urls import path

from recipes.views import contato, home, sobre

# dominio/recipes/
urlpatterns = [
    path('', home),  # Home
    path('contato/', contato),  # /contato/
    path('sobre/', sobre),  # /sobre/
]
