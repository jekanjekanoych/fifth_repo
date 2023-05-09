from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=25)

    def __str__(self):
        return "%s %s %i %i" % (self.first_name, self.last_name, self.age, self.id)
