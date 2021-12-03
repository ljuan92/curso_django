from django.db import models

# Create your models here.


class Theme(models.Model):
    name = models.CharField(max_length=30)


class Journalist(models.Model):
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    image_profile = models.ImageField(null=True)
    themes = models.ManyToManyField(Theme)


class News(models.Model):

    state_of_news = [
        ("E", "Editando"),
        ("P", "Publicado"),
        ("B", "Bloqueado")
    ]

    state = models.CharField(
        max_length=2,
        choices=state_of_news,
        default="E"
    )
    name = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(null=True)
    last_update_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=300)
    write_by = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE
    )
    main_image = models.ImageField(null=True)
