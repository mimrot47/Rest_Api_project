from rest_framework import serializers
from .models import Employee
def mut_1000(value):
    if value%1000 !=0:
        raise serializers.ValidationError('Salary multiple 1000')
# class EmployeeSerializers(serializers.Serializer):
#     eno= serializers.IntegerField()
#     ename=serializers.CharField(max_length=50)
#     esal=serializers.FloatField(validators=[mut_1000,])
#     eaddr=serializers.CharField(max_length=50)
#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.eno=validated_data.get('eno',instance.eno)
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eaddr=validated_data.get('eaddr',instance.eaddr)
#         instance.save()
#         return instance

class EmployeeSerializers(serializers.ModelSerializer):
    esal=serializers.FloatField(validators=[mut_1000,])
    class Meta:
        model=Employee 
        fields='__all__'

    def validate_esal(self,value):
        if value<5000:
            raise serializers.ValidationError('esal is greter than 5000')
        return value
    
    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower() == 'gokul':
            if esal <10000:
                raise serializers.ValidationError('salary shoul greter than 10000')
        return data
