from django.urls import path
from . import views

urlpatterns = [
    path('get-claims/<int:employee_id>/<str:permission>/<str:current>/', views.retrieve_claims, name='retrieve_claims'),
    path('update-claim/<int:claim_id>/<int:manager_id>/', views.update_claim, name='update_claim'),
    path('send-claim/', views.create_claim, name='create_claim'),
    path('delete-claim/', views.delete_claim, name='delete_claim'),
]
