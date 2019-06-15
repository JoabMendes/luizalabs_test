from django.conf.urls import url

from api.views import employee_view
from api.views import department_view

urlpatterns = [
    url(
        r'^department/?$',
        department_view.DepartmentAPIView.as_view()
    ),
    url(
        r'^employee/?(?P<id>[0-9]+)?/?$',
        employee_view.EmployeeAPIView.as_view()
    )
]
