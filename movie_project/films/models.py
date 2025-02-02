from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма')
    review = models.TextField('Отзыв о фильме')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'