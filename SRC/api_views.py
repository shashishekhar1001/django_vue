from rest_framework import viewsets
from .serializers import *
from .models import *

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer