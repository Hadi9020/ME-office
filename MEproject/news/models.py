from django.db import models
from members.models import Member
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Tag Name")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class News(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'

    class PublishedChoices(models.TextChoices):
        FRIEND = 'FR', 'Friends Only'
        CITY = 'CT', 'City Only'
        COUNTRY = 'CRT', 'Country Only'
        ALL = 'AL', 'All'

    author     = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='news')
    category   = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='news')
    tags       = models.ManyToManyField(Tag, related_name='news', verbose_name="Tags")
    
    title      = models.CharField(max_length=200, verbose_name="Title")
    text       = models.TextField(verbose_name="Content")
    summary    = models.CharField(max_length=300, blank=True, null=True, verbose_name="Summary")
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    
    image      = models.ImageField(upload_to="news/images/%Y/%m/%d", blank=True, null=True)
    video      = models.FileField(upload_to="news/videos/%Y/%m/%d", blank=True, null=True)
    
    likes      = models.PositiveIntegerField(default=0)
    dislikes   = models.PositiveIntegerField(default=0)
    views      = models.PositiveIntegerField(default=0)
    
    status     = models.CharField(max_length=2, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
    published  = models.CharField(max_length=3, choices=PublishedChoices.choices, null=True, blank=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
