from rest_framework.serializers import ModelSerializer
from .models import Employee
class EmpSelizers(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'