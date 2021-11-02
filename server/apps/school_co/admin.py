from django.contrib import admin

from .models import School, Pupil, LearnerTextGenre, ScanText, AnnotationType, PrintAnnotation, ScanPage, \
    ScanAnnotation, Region, Teacher, PrintText


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'education_level', 'school', 'teacher', 'region')
    list_filter = ('school', 'teacher')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'school')
    list_filter = ('school',)


@admin.register(LearnerTextGenre)
class LearnerTextGenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(ScanText)
class ScanTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'genre', 'date_published', 'name', 'pupil', 'teacher')
    list_filter = ('genre', 'pupil', 'teacher')


@admin.register(PrintText)
class PrintTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'genre', 'date_published', 'name', 'pupil', 'teacher', 'text')
    list_filter = ('genre', 'pupil', 'teacher')


@admin.register(ScanPage)
class ScanPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'file', 'object')


@admin.register(AnnotationType)
class AnnotationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'key')
    search_fields = ('name',)


@admin.register(PrintAnnotation)  # в обеих анн нет correct_text/comment -> занимают много места
class PrintAnnotationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'print_text',
        'begin_offset',
        'end_offset',
        'annotation_type',
        'checker',
    )
    list_filter = ('annotation_type', 'print_text')


@admin.register(ScanAnnotation)
class ScanAnnotationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'begin_offset_x', 'end_offset_x',
        'end_offset_y', 'begin_offset_y',
        'checker', 'ann_page', 'annotation_type'
    )
    list_filter = ('annotation_type', 'ann_page')
