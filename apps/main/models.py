from django.db import models

# Create your models here.

class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Зыголовок",
    )
    description = models.TextField(
        verbose_name="Описание",

    )
    banner = models.ImageField(
        upload_to= "banner/",
        verbose_name = "Фото",

    )
    logo = models.ImageField(
        upload_to = "Logo/",
        
        verbose_name = "Логотип"
    )

    def __str__(self):
        return self.title
    class Meta :
        verbose_name = "Настройка главной"
        verbose_name_plural = "Настройки главной"


class Over(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    date = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    direction = models.CharField(
        max_length=255,
        verbose_name="Направление"
    )
    img = models.ImageField(
        upload_to='over/',
        verbose_name="Фото"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Анимация"
        verbose_name_plural="Анимации"
