from rest_framework import serializers
from .models import Technology, Study, Validation


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'

class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = '__all__'