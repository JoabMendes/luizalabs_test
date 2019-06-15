from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from domain.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name'
        )


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email',
            'department'
        )
        depth = 1


class EmployeeWriteSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Employee.objects.all())]
    )

    class Meta:
        model = Employee
        fields = (
            'name',
            'email',
            'department'
        )
