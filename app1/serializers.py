from django.db import models
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import PrimeNumber

#create serializer using ModelSerializer

class PrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeNumber
        fields = ['id','in1','in2','out']
        read_only_fields = ['out']

    # AND overriding create method for needed output
    def create(self, validated_data):
        print(validated_data)
        in1 = validated_data.get('in1')
        in2 = validated_data.get('in2')
        out = []
        
        if in1 >= 0:
            for i in range(in1,in2 + 1):  
                for j in range(2,i):  
                    if (i % j) == 0:
                        break  
                else:
                    out.append(i)
            if out[0]==1 or out[1]==1 :
                out.remove(1)
                if out[0]==0:
                    out.remove(0)
            a =','.join(map(str, out))   
            validated_data.update({'out':a})
        return super().create(validated_data)