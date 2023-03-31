from rest_framework import viewsets
from .serializers import EmpSerializer
from .models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EmpViewSet(viewsets.ModelViewSet):
    serializer_class = EmpSerializer
    queryset = Employee.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    