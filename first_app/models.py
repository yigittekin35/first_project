from django.db import models

# python manage.py migrate
# python manage.py makemigrations first_app
# python manage.py migrate

class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.PROTECT)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete = models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    e_mail = models.CharField(max_length = 264)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
