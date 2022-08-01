from django.db import models


class Quiz(models.Model):
    pergunta = models.CharField(max_length=128, unique=True)
    descricao = models.TextField()
    autor = models.CharField(max_length=128, unique=True)
    imagem = models.URLField(
        max_length=1024,
    )

    def __str__(self):
        return self.pergunta
