from rest_framework import serializers
from .models import Incident, Report

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'incident_id',
            'title',
            'date',
            'description'
        )
        model = Incident