from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token  


class User(AbstractUser):
    PERFIL = (
        ('microempreendedor', 'Microempreendedor'),
        ('desenvolvedor', 'Desenvolvedor'),
    )
    perfil = models.CharField(max_length=17, choices=PERFIL)

##gambiarra
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='sisteminha_user_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='sisteminha_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class Desenvolvedor(User):
    cpf = models.CharField(max_length=11, unique=True)
    foto = models.ImageField(upload_to='imgs/desenvolvedores', default=f'imgs/avatar.png')
    descricao = models.TextField(default="Descrição está vazia.")
    github = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Microempreendedor(User):
    cnpj = models.CharField(max_length=14, unique=True)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='imgs/microempreendedores', default=f'imgs/avatar.png')

    def __str__(self):
        return self.username