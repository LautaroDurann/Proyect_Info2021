from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion= timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

class Comentario(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	contenido = models.TextField(max_length=500)
	fecha_hora = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.contenido

	class Meta:
		verbose_name = ("Comentario")
		verbose_name_plural= ("Comentarios")
