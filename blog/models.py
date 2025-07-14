import itertools

from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.db import models
from django.urls import reverse


user = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"post_slug": self.slug})

    def _generate_slug(self):
        slug = slugify(self.title)

        for i in itertools.count(1):
            if not Post.objects.filter(slug=slug).exists():
                break
            slug = f"{slug}-{i}"

        self.slug = slug

    def save(self, *args, **kwargs):

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

