from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from school_co.serializers import SchoolSerializer, PupilSerializer, LearnerTextGenreSerializer, LearnerTextSerializer, AnnotationTypeSerializer, LearnerTextAnnotationSerializer
from school_co.models import School, Pupil, LearnerTextGenre, LearnerText, AnnotationType, LearnerTextAnnotation


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer



class LearnerTextGenreViewSet(viewsets.ModelViewSet):
    queryset = LearnerTextGenre.objects.all()
    serializer_class = LearnerTextGenreSerializer



class LearnerTextViewSet(viewsets.ModelViewSet):
    queryset = LearnerText.objects.all()
    serializer_class = LearnerTextSerializer



class AnnotationTypeViewSet(viewsets.ModelViewSet):
    queryset = AnnotationType.objects.all()
    serializer_class = AnnotationTypeSerializer



class LearnerTextAnnotationViewSet(viewsets.ModelViewSet):
    queryset = LearnerTextAnnotation.objects.all()
    serializer_class = LearnerTextAnnotationSerializer


