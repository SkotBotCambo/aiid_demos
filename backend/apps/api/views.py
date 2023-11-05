from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Incident, Report
from .serializers import IncidentSerializer

# Create your views here.
class ListIncident(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class DetailIncident(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

# api views a la this project: https://github.com/baris5d/DjangoReact/blob/master/books/views.py


@api_view(['GET'])
def incidents_list(request, *args, **kwargs):
    ilist = Incident.objects.all()
    incidents = [x.serialize() for x in ilist]
    data = {
        "response": incidents
    }

    return Response(data)

@api_view(['GET'])
def incident_detail_view(request, incident_id, *args, **kwargs):
    data = {
        "incident_id":incident_id
    }
    status = 200
    try:
        obj = Incident.objects.get(incident_id=incident_id)
        data['title'] = obj.title
        data['description'] = obj.description
        data['status'] = 'ok',
        data['id'] = obj.incident_id

    except:
        data['message'] = "Not Found"
        data['status'] = "Error"

    return Response(data, status=status)

@api_view(['POST'])
def incident_create_view(request, *args, **kwargs):
    print(request.POST)
    serializer = IncidentSerializer(data=request.data or None)
    
    return Response(serializer.data)