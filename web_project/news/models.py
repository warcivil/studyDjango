from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='дата создания')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='дата редактирования')
    photo=models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='фото', blank = True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано?')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', '-title']
