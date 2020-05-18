from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class Project(models.Model):
    CATEGORY_CHOICES = (('com', 'Commercial'),
                        ('tv', 'TV'),
                        ('cr', 'Creative'))

    title = models.CharField('Назва проекту', max_length=60)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField('Зображення', upload_to='images/works')
    video_url = models.URLField('Url vimeo')
    description = HTMLField('Опис проекту')
    description_short = models.TextField(max_length=300)
    category = models.CharField('Категорія', max_length=225, choices=CATEGORY_CHOICES, default='com')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'


class Partner(models.Model):
    name = models.CharField('Назва',
                            max_length=125,
                            help_text='Назва')
    image = models.ImageField('Зображення',
                              upload_to='images/partners',
                              null=True,
                              blank=True)
    link = models.URLField('Посилання',
                           null=True,
                           blank=True,
                           default='#')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'


@receiver(post_delete)
def submission_delete(sender, instance, **kwargs):
    try:
        instance.image.delete(False)
    except AttributeError:
        pass
