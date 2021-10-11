from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class School(models.Model):
    name = models.CharField(
        max_length=128,
        help_text="название школы в которой учится ученик"
    )

class Pupil(models.Model):
    full_name = models.CharField(max_length=128, help_text="ФИО")
    education_level = models.IntegerField(help_text="класс")
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    # регион

class LearnerTextGenre(models.Model):
    title = models.CharField(max_length=128, help_text="человекочитаемое название жанра")

class LearnerText(models.Model):
    class Status(models.IntegerChoices):
        NEW = 1
        CHECKED = 10

    text = models.TextField()
    # скан (будет добавлено как позже как ссылка на модель файлов)
    status = models.IntegerField(choices=Status.choices)
    genre = models.ForeignKey('LearnerTextGenre', on_delete=models.PROTECT)

class AnnotationType(models.Model):
    name = models.CharField(max_length=64, help_text="человекочитаемое название")
    key = models.CharField(
        max_length=64,
        help_text="ключи являются materialized path и позволяют делать из типов аннотаций иерархичную структуру")

class LearnerTextAnnotation(models.Model):
    learner_text = models.ForeignKey('LearnerText', on_delete=models.PROTECT)
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
