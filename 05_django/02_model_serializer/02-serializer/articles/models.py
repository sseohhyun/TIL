from django.db import models

# Create your models here.
class Articel(models.Modes):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ac = models.DateTimeField(auto_now=True)

    def __str__(self):
        # print 했을 때 사람이 보기 좋게 꾸밀 때 사용함
        return self.title
    