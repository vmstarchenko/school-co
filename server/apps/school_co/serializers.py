from rest_framework import serializers
from .models import School, Pupil, LearnerTextGenre, LearnerText, AnnotationType, LearnerTextAnnotation, LearnerTextScanPage

from base.serializers import BaseUploadedFileSerializer


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = [
            'id', 'url',
            'name',
        ]


class PupilSerializer(serializers.HyperlinkedModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Pupil
        fields = [
            'id', 'url',
            'full_name',
            'education_level',
            'school',
        ]


class LearnerTextGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnerTextGenre
        fields = [
            'id', 'url',
            'title',
        ]


class LearnerTextSerializer(serializers.HyperlinkedModelSerializer):
    genre = LearnerTextGenreSerializer()

    class Meta:
        model = LearnerText
        fields = [
            'id', 'url',
            'text',
            'status',
            'genre',
        ]


class AnnotationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnnotationType
        fields = [
            'id', 'url',
            'name',
            'key',
        ]


class LearnerTextAnnotationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnerTextAnnotation
        fields = '__all__'


class LearnerTextScanPageSerializer(BaseUploadedFileSerializer):
    class Meta:
        model = LearnerTextScanPage
        fields = '__all__'
