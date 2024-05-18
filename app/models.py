from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Categories"


class Detail(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        db_table = "Details"
