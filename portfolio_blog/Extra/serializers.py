from rest_framework import serializers
from .models import Technology, Study, Validation


class TechnologySerializer(serializers.ModelSerializer):
    validations = serializers.IntegerField(source='get_validations_count', read_only=True)
    class Meta:
        model = Technology
        fields = '__all__'

class StudySerializer(serializers.ModelSerializer):
    validations = serializers.IntegerField(source='get_validations_count', read_only=True)
    class Meta:
        model = Study
        fields = '__all__'

class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = '__all__'