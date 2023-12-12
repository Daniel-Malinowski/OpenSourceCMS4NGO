from django.db import models

# Create your models here.


class Admin(models.Model):
    name = models.CharField(
        max_length=100, blank=False, verbose_name='Nazwa Użytkownika')
    email = models.EmailField(
        max_length=100, blank=False, verbose_name='Adres email')
    password = models.CharField(
        min_length=8, max_length=16, blank=False, verbose_name='Hasło')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'
        ordering = ['name']
