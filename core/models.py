# from django.contrib.auth.models import UserManager
#from django.conf import settings

from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo

# class Post(models.Model):
#     autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
#     titulo = models.CharField('Título', max_length=100)
#     texto = models.TextField('Texto', max_length=400)

#     def __str__(self):
#         return self.titulo

'''
class Post(models.Model):
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
'''
