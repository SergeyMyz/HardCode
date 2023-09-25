from django.db import models


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    link = models.URLField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    lesson_id = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    products = models.ManyToManyField(Product, blank=True)
    lessons = models.ManyToManyField(Lesson, through='View')

    def __str__(self):
        return f"{self.name} {self.surname}"


class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewing_duration = models.IntegerField(blank=True)
    viewed = models.BooleanField(default=False)
    view_date = models.DateField(blank=True)

    def __str__(self):
        return f"{self.user} {self.lesson}"


