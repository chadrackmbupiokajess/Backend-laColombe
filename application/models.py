from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='services/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Equipe(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='equipe/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Equipement(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='equipements/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Space(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='spaces/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
