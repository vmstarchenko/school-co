from django.contrib import admin

from .models import School, Pupil, LearnerTextGenre, LearnerText, AnnotationType, LearnerTextAnnotation, LearnerTextScanPage


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'education_level', 'school')
    list_filter = ('school',)


@admin.register(LearnerTextGenre)
class LearnerTextGenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(LearnerText)
class LearnerTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'status', 'genre')
    list_filter = ('genre',)


@admin.register(AnnotationType)
class AnnotationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'key')
    search_fields = ('name',)


@admin.register(LearnerTextAnnotation)
class LearnerTextAnnotationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'learner_text',
        'begin_offset',
        'end_offset',
        'correct_text',
        'comment',
        'annotation_type',
        'checker',
    )
    list_filter = ('annotation_type',)


@admin.register(LearnerTextScanPage)
class LearnerTextScanPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'file', 'object')
