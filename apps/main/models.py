from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Загаловок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    banner = models.ImageField(
        upload_to='banner/',
        verbose_name='Фото баннера'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка главной'
        verbose_name_plural = 'Настройки главной'

class Awarts(models.Model):
    image = models.ImageField(
        upload_to='awarts/',
        verbose_name='Фото'
    )

    def __str__(self):
        return f"{self.image}"
    
    class Meta:
        verbose_name = "Фото (about)"
        verbose_name_plural = "Фотки (about)"

class Contact(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Загаловок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    phone = models.BigIntegerField(
        verbose_name="Номер телефона"
    )
    title_2 = models.CharField(
        max_length=255,
        verbose_name="Нижний загаловок"
    )
    description_2 = models.TextField(
        verbose_name="Описание нижнего загаловка"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Загаловок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    video = models.FileField(
        upload_to="video/",
        verbose_name="Видео"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка (about)'
        verbose_name_plural = 'Настройки (about)'


class Form(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя отпровителя"
    )
    email = models.EmailField(
        verbose_name="email отпровителя"
    )
    message = models.TextField(
        verbose_name="Сщщбщение"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Оставленный отзыв'
        verbose_name_plural = 'Оставленные отзывы'


class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользовотеля"
    )
    user_name = models.CharField(
        max_length=100,
        verbose_name="Имя пользователя",
        null=True, blank=True
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        null=True, blank=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return str(self.user_name)
    
    class Meta:
        verbose_name = 'Пользователь телегрм'
        verbose_name_plural = 'Пользователи телегрма'