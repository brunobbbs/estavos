from django.db import models


class BannerManager(models.Manager):
    def get_queryset(self):
        queryset = super(BannerManager, self).get_queryset()
        queryset = queryset.filter(active=True)
        return queryset


class Banner(models.Model):
    title = models.CharField('Título', max_length=150)
    description = models.CharField('Descrição', max_length=300, blank=True)
    action_name = models.CharField('Nome do botão de ação', max_length=50)
    target = models.URLField('Link do botão')
    image = models.ImageField(
        upload_to='home/banners/',
        verbose_name='Imagem',
        help_text='Use uma imagem com tamanho de 1600x575'
    )
    active = models.BooleanField('Ativo', default=True)

    objects = models.Manager()
    actives = BannerManager()

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField('Nome', max_length=150)
    site = models.URLField('Site', blank=True, null=True)
    image = models.ImageField(
        upload_to='home/partners/',
        verbose_name='Logo do parceiro',
        help_text='Use uma imagem com tamanho de 212x65'
    )
    active = models.BooleanField('Ativo', default=True)

    objects = models.Manager()
    actives = BannerManager()

    def __str__(self):
        return self.name
