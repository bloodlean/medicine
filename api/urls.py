from django.urls import path
from .views import (
    ClientAPI,
    ClientDetailAPI,
    BlogAPI,
    BlogDetailAPI,
    SponsorAPI,
    SponsorDetailAPI,
)

urlpatterns = [
    path('client/', ClientAPI.as_view(), name='client'),
    path('client/<int:pk>/', ClientDetailAPI.as_view(), name='client-detail'),
    path('blog/', BlogAPI.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailAPI.as_view(), name='blog-detail'),
    path('sponsor/', SponsorAPI.as_view(), name='sponsor'),
    path('sponsor/<int:pk>/', SponsorDetailAPI.as_view(), name='sponsor-detail')
]