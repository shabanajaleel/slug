from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.fnhome,name="home"),
    path('view_book/<slug>',views.fnviewbook,name="view_book"),
]