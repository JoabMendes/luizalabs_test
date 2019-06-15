# Models
from domain.models import Employee

# Rest Framework libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Custom permissions
from api.custom_permissions import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication

# Serializers
from api.serializers import EmployeeSerializer, EmployeeWriteSerializer


class EmployeeAPIView(APIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication
    )
    permission_classes = ()

    def get_employee(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """" GET /api/v1/employee

            Retrieves a list of employees
            Pagination can be enabled with parameters:
            >>>> {
                'pagination': true,
                'offset': 0, # Default 0
                'employees_per_page': 10, # Deafult 10
            }
        """

        # Pagination controls
        offset = 0
        employees_per_page = 10
        if 'offset' in request.GET:
            offset = int(request.GET['offset'])
        if 'employees_per_page' in request.GET:
            employees_per_page = int(request.GET['employees_per_page'])

        # Get objects queryset
        employees = Employee.objects.all()

        if 'pagination' in request.GET:
            # If pagination is active, let's slice the queryset
            employees = employees[offset:(offset + employees_per_page)]

        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        """" POST /api/v1/employee

            Creates an Employee instance:
            >>>>> payload: {
                name: 'Employee Name',
                email: 'Employee name',
                department: '<department_id>'
             }
        """
        serializer = EmployeeWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        """" PUT /api/v1/employee/<id>

            Edits an employee information
        """
        employee = self.get_employee(pk=id)
        serializer = EmployeeWriteSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id, format=None):
        """" DELETE /api/v1/employee/<id>

            Deletes a specified employee
        """
        employee = self.get_employee(pk=id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
