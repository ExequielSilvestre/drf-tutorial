from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    finish_date = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']