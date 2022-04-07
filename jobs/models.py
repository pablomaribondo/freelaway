from django.db import models
from django.contrib.auth.models import User


class Reference(models.Model):
    file = models.FileField(upload_to='references')

    def __str__(self) -> str:
        return self.file.url


class Job(models.Model):
    category_choices = (('D', 'Design'),
                        ('EV', 'Edição de Vídeo'))

    status_choices = (('C', 'Em criação'),
                      ('AA', 'Aguardando aprovação'),
                      ('F', 'Finalizado'))

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=2, choices=category_choices, default="D")
    deadline = models.DateTimeField()
    price = models.FloatField()
    references = models.ManyToManyField(Reference)
    professional = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)
    reserved = models.BooleanField(default=False)
    status = models.CharField(
        max_length=2, choices=status_choices, default='AA')

    def __str__(self) -> str:
        return self.title
