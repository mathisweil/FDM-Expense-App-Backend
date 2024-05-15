from django.urls import path
from . import views

urlpatterns = [
    path('claims/', views.claims_list, name='claims_list'),
    path('claims/<int:pk>/', views.claim_detail),
]