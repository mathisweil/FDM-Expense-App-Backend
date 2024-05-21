from datetime import date
from .models import Claim
from users.models import Employee
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClaimSerializer


# Create your views here.

@api_view(['POST'])
def create_claim(request):
    serializer = ClaimSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_claims(request, employee_id, permission, current):
    current = current.lower() == 'true'
    try:
        if permission == 'EMPLOYEE':
            if current:
                claims = Claim.objects.filter(Q(employee_id=employee_id) & ~Q(status='PROCESSED'))
            else:
                claims = Claim.objects.filter(Q(employee_id=employee_id) & Q(status='PROCESSED'))
        elif permission == 'MANAGER':
            if current:
                claims = Claim.objects.filter(Q(employee_id__manager_id=employee_id) & (Q(status='PENDING') | Q(status='REJECTEDF')))
            else:
                claims = Claim.objects.filter(
                    Q(employee_id__manager_id=employee_id) & (Q(status='PROCESSED') | Q(status='APPROVED') | Q(status='REJECTED')))
        elif permission == 'FINANCE':
            if current:
                claims = Claim.objects.filter(Q(employee_id__finance_id=employee_id) & Q(status='APPROVED'))
            else:
                claims = Claim.objects.filter(
                    Q(employee_id__finance_id=employee_id) & (Q(status='PROCESSED') | Q(status='REJECTEDF')))
        else:
            claims = Claim.objects.all()
        serializer = ClaimSerializer(claims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_claim(request, claim_id, manager_id):
    claim = get_object_or_404(Claim, claim_id=claim_id)
    employee = get_object_or_404(Employee, employee_id=manager_id)
    if employee.permission == 'MANAGER' or employee.permission == 'FINANCE':
        if request.data['status'].upper() == 'APPROVED':
            claim.approved_on = date.today()
            claim.approved_by = employee.first_name + " " + employee.last_name
        elif request.data['status'].upper() == 'REJECTEDF':
            claim.approved_on = None
            claim.approved_by = None
    serializer = ClaimSerializer(claim, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_claim(request, claim_id):
    claim = get_object_or_404(Claim, claim_id=claim_id)
    claim.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
