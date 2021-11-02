from rest_framework import serializers
from .models import School, Pupil, LearnerTextGenre, ScanText, AnnotationType, \
    ScanPage, ScanAnnotation, Region, Teacher, PrintText, PrintAnnotation

from base.serializers import BaseUploadedFileSerializer


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = [
            'id', 'url',
            'name',
        ]


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = [
            'id', 'url',
            'name',
        ]


class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = [
            'id', 'url',
            'full_name', 'school',
        ]


class PupilSerializer(serializers.HyperlinkedModelSerializer):
    school = SchoolSerializer()
    region = RegionSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Pupil
        fields = [
            'id', 'url',
            'full_name',
            'education_level',
            'school', 'region',
            'teacher'
        ]


class LearnerTextGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnerTextGenre
        fields = [
            'id', 'url',
            'title',
        ]


class ScanTextSerializer(serializers.HyperlinkedModelSerializer):
    genre = LearnerTextGenreSerializer()
    pupil = PupilSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = ScanText
        fields = [
            'id', 'url',
            'status',
            'genre', 'date_published',
            'name', 'marked', 'teacher', 'pupil',
        ]


class PrintTextSerializer(serializers.HyperlinkedModelSerializer):
    genre = LearnerTextGenreSerializer()
    pupil = PupilSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = PrintText
        fields = [
            'id', 'url',
            'text',
            'status',
            'genre', 'date_published',
            'name', 'marked', 'text', 'pupil', 'teacher'
        ]


class ScanPageSerializer(BaseUploadedFileSerializer):
    object = ScanTextSerializer()
    class Meta:
        model = ScanPage
        fields = '__all__'


class AnnotationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnnotationType
        fields = [
            'id', 'url',
            'name',
            'key',
        ]


class ScanAnnotationSerializer(serializers.HyperlinkedModelSerializer):
    ann_page = ScanPageSerializer()
    annotation_type = AnnotationTypeSerializer()
    class Meta:
        model = ScanAnnotation
        fields = [
            'begin_offset_x', 'end_offset_x',
            'end_offset_y', 'begin_offset_y', 'correct_text',
            'comment', 'annotation_type', 'ann_page']


class PrintAnnotationSerializer(serializers.HyperlinkedModelSerializer):
    print_text = PrintTextSerializer()
    annotation_type = AnnotationTypeSerializer()
    class Meta:
        model = PrintAnnotation
        fields = [
            'begin_offset', 'end_offset',
            'correct_text',
            'comment', 'annotation_type', 'print_text']


