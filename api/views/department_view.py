# Models
from domain.models import Department

# Rest Framework libraries
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from api.serializers import DepartmentSerializer


class DepartmentAPIView(APIView):

    permission_classes = ()

    def get(self, format=None):
        """" GET /api/v1/department

            Retrieves a list of departments
        """
        # Get objects queryset
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
