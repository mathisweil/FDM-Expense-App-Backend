from django.shortcuts import render, get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_employees(request, permission, employee_id):
    try:
        if permission == 'MANAGER':
            employees = Employee.objects.filter(employee_id=employee_id)
        elif permission == 'FINANCE':
            employees = Employee.objects.filter(finance_id=employee_id)
        else:
            employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def retrieve_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    serializer = EmployeeSerializer(employee, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
