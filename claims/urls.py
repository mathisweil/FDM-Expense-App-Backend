from django.urls import path
from . import views

urlpatterns = [
    path('get-claims/<str:permission>/<boolean:current>/<int:user_id>/', views.get_claims, name='get_claims'),
    path('update-claim/<int:user_id>/<int:current>/<int:user_id>/', views.update_claim, name='update_claim'),
    path('send-claim/', views.create_claim, name='create_claim'),
]
