from django.urls import path
from . import views

urlpatterns = [
    path('', views.categ),
    path('<int:id>/', views.catedetails)
]