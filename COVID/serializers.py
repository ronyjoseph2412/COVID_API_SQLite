from rest_framework import serializers
from COVID.models import COVID_India

class COVID_India_Serializer(serializers.ModelSerializer):
    class Meta:
        model=COVID_India
        fields=('Region','Total_Cases','Positive_Cases_Today','Active_Cases','Total_Cases_Recovered','Daily_Cases_Recovered','Confirmed_Deaths','Deaths_Per_Day','Active_Cases_Ratio')