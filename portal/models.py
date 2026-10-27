from django.core.exceptions import ValidationError
from django.db import models


class Conteudo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo_html = models.TextField(
        help_text='Estrutura HTML interna da página (sem html, head, body, header, nav ou footer)'
    )
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'

    def __str__(self):
        return self.titulo


class Menu(models.Model):
    TIPO_CHOICES = (
        ('interno', 'Conteúdo interno'),
        ('externo', 'Link externo'),
    )

    titulo = models.CharField(max_length=100)
    tipo_destino = models.CharField(
        max_length=10, choices=TIPO_CHOICES, default='interno'
    )
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='menus',
        help_text='Preencher somente se o tipo for "Conteúdo interno"',
    )
    url_externa = models.URLField(
        blank=True,
        null=True,
        help_text='Preencher somente se o tipo for "Link externo"',
    )

    class Meta:
        verbose_name = 'Item do menu'
        verbose_name_plural = 'Itens do menu'
        ordering = ['ordem']

    def clean(self):
        if self.tipo_destino == 'interno' and not self.conteudo:
            raise ValidationError('Selecione um conteúdo para links internos.')
        if self.tipo_destino == 'externo' and not self.url_externa:
            raise ValidationError('Informe a URL para links externos.')

    def __str__(self):
        return self.titulo
