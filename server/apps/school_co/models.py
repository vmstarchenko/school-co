from django.db import models
from django.contrib.auth import get_user_model
from base.models import BaseUploadedFile

User = get_user_model()


class School(models.Model):
    name = models.CharField(
        max_length=128,
        help_text="название школы в которой учится ученик"
    )
    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(
        max_length=128,
        help_text="регион РФ, где живет ученик"
    )
    def __str__(self):
        return self.name


class Pupil(models.Model):
    full_name = models.CharField(max_length=128, help_text="ФИО")
    education_level = models.IntegerField(help_text="класс")
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    region = models.ForeignKey('Region', on_delete=models.PROTECT)
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)
    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    full_name = models.CharField(max_length=128, help_text="ФИО")
    school = models.ForeignKey('School', on_delete=models.PROTECT)  # many-to-many вызывает ошибку -????
    def __str__(self):
        return self.full_name


class LearnerTextGenre(models.Model):
    title = models.CharField(max_length=128, help_text="человекочитаемое название жанра")
    def __str__(self):
        return self.title


class ScanText(models.Model):
    class Status(models.IntegerChoices):
        NEW = 1
        CHECKED = 10

    class Marked(models.IntegerChoices):
        MARKED = 1
        UNMARKED = 0

    date_published = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=128, help_text="название текста")
    genre = models.ForeignKey('LearnerTextGenre', on_delete=models.PROTECT)
    pupil = models.ForeignKey('Pupil', on_delete=models.PROTECT)
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)
    status = models.IntegerField(choices=Status.choices)
    marked = models.IntegerField(choices=Marked.choices)
    def __str__(self):
        return self.name


class PrintText(models.Model):
    class Status(models.IntegerChoices):
        NEW = 1
        CHECKED = 10

    class Marked(models.IntegerChoices):
        MARKED = 1
        UNMARKED = 0
    text = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=128, help_text="название текста")
    genre = models.ForeignKey('LearnerTextGenre', on_delete=models.PROTECT)
    pupil = models.ForeignKey('Pupil', on_delete=models.PROTECT)
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)
    status = models.IntegerField(choices=Status.choices)
    marked = models.IntegerField(choices=Marked.choices)

    def __str__(self):
        return self.name


class ScanPage(BaseUploadedFile):
    file = models.ImageField(upload_to='learner_text_scan_page')
    n = models.PositiveSmallIntegerField(
        help_text="номер страницы")
    object = models.ForeignKey(
        'ScanText',
        on_delete=models.PROTECT,
        null=True, blank=True,
    )

    def __str__(self):
        return self.object.name + " " + str(self.n)


class AnnotationType(models.Model):
    name = models.CharField(max_length=64, help_text="человекочитаемое название")
    key = models.CharField(
        max_length=64,
        help_text="ключи являются materialized path и позволяют делать из типов аннотаций иерархичную структуру")

    def __str__(self):
        return self.name


class PrintAnnotation(models.Model):
    print_text = models.ForeignKey('PrintText', on_delete=models.PROTECT)
    begin_offset = models.PositiveSmallIntegerField(
        help_text="offset начала аннотации")
    end_offset = models.PositiveSmallIntegerField(
        help_text="offset окончания аннотации")

    correct_text = models.TextField(
        blank=True,
        help_text="иcправление аннотации (текст с правильный вариантом. Если в изначальном тексте подстроку [offset_begin:offset_end] заменить на исправление, то должен получиться корректный текст)")

    comment = models.TextField(blank=True, default="")
    annotation_type = models.ForeignKey('AnnotationType', on_delete=models.PROTECT)
    checker = models.ForeignKey(User, on_delete=models.PROTECT)


class ScanAnnotation(models.Model):
    ann_page = models.ForeignKey('ScanPage', on_delete=models.PROTECT)

    begin_offset_x = models.PositiveSmallIntegerField(
        help_text="offset x начала аннотации")
    end_offset_x = models.PositiveSmallIntegerField(
        help_text="offset x окончания аннотации")
    begin_offset_y = models.PositiveSmallIntegerField(
        help_text="offset y начала аннотации")
    end_offset_y = models.PositiveSmallIntegerField(
        help_text="offset y окончания аннотации")

    correct_text = models.TextField(
        blank=True,
        help_text="иcправление аннотации (текст с правильный вариантом. Если в изначальном тексте подстроку [offset_begin:offset_end] заменить на исправление, то должен получиться корректный текст)")
    comment = models.TextField(blank=True, default="")
    annotation_type = models.ForeignKey('AnnotationType', on_delete=models.PROTECT)
    checker = models.ForeignKey(User, on_delete=models.PROTECT)



