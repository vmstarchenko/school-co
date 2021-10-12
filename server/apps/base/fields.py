import functools

from django.db import models


CreatedField = functools.partial(
    models.DateTimeField,
    auto_now_add=True)
