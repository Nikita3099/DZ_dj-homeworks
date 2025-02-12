from django.db import models
from django.core.exceptions import ValidationError

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    tags = models.ManyToManyField('Tag', through='Scope')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="scopes")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_main', 'tag__name']

    def clean(self):
        if self.is_main and Scope.objects.filter(article=self.article, is_main=True).exclude(pk=self.pk).exists():
            raise ValidationError("У статьи может быть только один основной тег.")

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"
