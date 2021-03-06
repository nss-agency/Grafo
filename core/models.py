from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    CATEGORY_CHOICES = (
        ('exp', _('Explainers')),
        ('com', _('Commercials')),
        ('mus', _('Music videos')),
        ('logo', _('Logo animation')),
        ('cr', _('Creative'))
    )
    PLACEMENT_CHOICES = (('main', 'Main Page'),
                         ('projects', 'Project Page'))

    title = models.CharField('Назва проекту', max_length=60)
    slug = AutoSlugField(populate_from='title')
    meta_title = models.TextField('Мета Заголовок')
    meta_description = models.TextField('Мета Опис')
    image = models.ImageField('Зображення', upload_to='images/works')
    video_url = models.URLField('Url')
    description = HTMLField('Опис проекту')
    description_short = models.TextField(max_length=300)
    category = models.CharField('Категорія', max_length=225, choices=CATEGORY_CHOICES, default='com')
    placement = models.CharField('Розташування проекту', max_length=225, choices=PLACEMENT_CHOICES, default='projects')

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
                              upload_to='images/partners')
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
