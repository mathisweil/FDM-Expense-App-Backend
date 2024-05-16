from django.shortcuts import render
from django.http import HttpResponse
from .models import Claim
from django.db.models import Q


# Create your views here.

def get_claims(request):
    if permission == 'EMPLOYEE':
        if current:
            claims = Claim.objects.filter(Q(employee_id=request.user_id) & ~Q(status='COMPLETED'))
        else:
            claims = Claim.objects.filter(Q(employee_id=request.user_id) & Q(status='COMPLETED'))
    elif permission == 'MANAGER':
        if current:
            claims = Claim.objects.filter(Q(manager_id=request.user_id) & (Q(status='PENDING') | Q(status='REJECTEDF')))
        else:
            claims = Claim.objects.filter(
                Q(manager_id=request.user_id) & (Q(status='COMPLETED') | Q(status='APPROVED') | Q(status='REJECTED')))
    elif permission == 'FINANCE':
        if current:
            claims = Claim.objects.filter(Q(employee_id=request.user_id) & ~Q(status='APPROVED'))
        else:
            claims = Claim.objects.filter(
                Q(employee_id=request.user_id) & (Q(status='PROCESSED') | Q(status='REJECTEDF')))
    else:
        claims = Claim.objects.all()
    return render(request, 'claims/claims.html', {'claims': claims})


def update_claim(request, claim_id):
    claim = Claim.objects.get(claim_id=claim_id)
    claim.status = 'APPROVED'
    claim.save()
    return HttpResponse('Claim approved')


def send_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.employee_id = request.user_id
            claim.save()
            return HttpResponse('Claim submitted')
    else:
        form = ClaimForm()
    return render(request, 'claims/send_claim.html', {'form': form})

def create_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.employee_id = request.user_id
            claim.save()
            return HttpResponse('Claim submitted')
    else:
        form = ClaimForm()
    return render(request, 'claims/send_claim.html', {'form': form})