from django.urls import path
from gallery.views import *

urlpatterns = [
    path('', GalleyAPIView.as_view()),
    path('<int:id>/', GalleryDetailView.as_view())

]