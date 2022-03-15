from django.db import models
from django.contrib.auth import get_user_model


class TvShow(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='')
    rating = models.IntegerField(default=0)
    rater = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.rating} {self.rater}'
