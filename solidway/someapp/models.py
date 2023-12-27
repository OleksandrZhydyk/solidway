from django.db import models


class SomeModel(models.Model):
    first_field = models.CharField(max_length=128)
    second_field = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_field

    class Meta:
        ordering = ("first_field",)
        verbose_name_plural = "SomeModels"
