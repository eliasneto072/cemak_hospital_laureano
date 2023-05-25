from django.db import models


class Noticia(models.Model):
    manchete = models.CharField(max_length=200)
    materia = models.CharField(max_length=1000)
    link_imagem = models.URLField(null=True)
    imagem = models.ImageField('imagem_noticia',upload_to='Imagens',null=True)
    autor = models.CharField(max_length=200)
    data = models.DateTimeField(null=True, auto_now_add=True)
    categoria = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Notícias'
        verbose_name = 'Notícia'

    def __str__(self):
        return self.manchete


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    link_video = models.URLField(null=True)
    thumbnail = models.ImageField('Thumbnail',upload_to='Thumbnail', null=True, blank=True)
    descricao = models.CharField(max_length=500)
    data = models.DateTimeField(null=True, auto_now_add=True)
    autor = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Vídeos'
        verbose_name = 'Vídeo'

    def __str__(self):
        return self.titulo


class Banner(models.Model):
    nome = models.CharField(verbose_name='Nome banner', max_length=10, null=False, blank=False)

    CHOICES = (
    ("4", "1"),
    ("3", "2"),
    ("2", "3"),
    ("1", "4"),
    )
    posicao = models.CharField('', max_length=1, choices=CHOICES, null=True, blank=True, unique=True)
    imagem = models.ImageField('Banner', upload_to='Banner', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Banners'

    def str(self):
        return self.nome




class Footer(models.Model):
    endereco =models.CharField(verbose_name='Endereço',max_length=100,null=False,)
    localizacao =models.CharField(verbose_name='localização',max_length=100,null=False)
    contato = models.IntegerField(verbose_name='Contato',default=(' +55 (00) 9'))
    saiba_mais = models.CharField(verbose_name='Saiba mais',max_length=100,null=False)

    class Meta:
        verbose_name = 'Rodapé'

    def str(self) -> str:
        return self.endereco
    
