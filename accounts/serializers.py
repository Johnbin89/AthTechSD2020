from rest_framework import serializers
from .models import Regulation, SubField

class RegulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regulation
        fields = "__all__"


class SubFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubField
        fields = "__all__"