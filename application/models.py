from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class EquipeCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Catégorie d'équipe"
        verbose_name_plural = "Catégories d'équipe"

    def __str__(self):
        return self.name


class Equipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(EquipeCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='members')
    role = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='equipe/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Equipement(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='equipements/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Space(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='spaces/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Utilisateur(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, default='')
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=200, default='Utilisateur')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Notification(models.Model):
    TYPE_INFO = 'info'
    TYPE_SUCCESS = 'success'
    TYPE_WARNING = 'warning'
    TYPE_ALERT = 'alert'

    NOTIFICATION_TYPES = [
        (TYPE_INFO, 'Information'),
        (TYPE_SUCCESS, 'Succès'),
        (TYPE_WARNING, 'Avertissement'),
        (TYPE_ALERT, 'Alerte'),
    ]

    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default=TYPE_INFO)
    link = models.CharField(max_length=255, blank=True, default='')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
