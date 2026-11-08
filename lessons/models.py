from django.db import models

# Create your models here.
class Lesson(models.Model):
    # the number of the lesson in order
    # 
    order = models.PositiveSmallIntegerField() # 0 means lesson is not displayed
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="", null=False)
    # the lesson body should allow for <html> elements to display for subheadings
    # how to do this: {{ body.content|safe }} when we want to render the content
    # this is unsafe if we allow users to upload lessons
    body = models.TextField()

