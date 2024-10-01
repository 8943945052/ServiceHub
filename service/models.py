from django.db import models

# Create your models here.


class Customers(models.Model):

    name = models.CharField(max_length=200)

    phone=models.CharField(max_length=200)

    email = models.EmailField(max_length=200)

    vehicle_number=models.CharField(max_length=200)

    running_kilometer=models.IntegerField()

    work_options=(
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),        
    )

    status=models.CharField(max_length=200,choices=work_options)

    def __str__(self):

        return self.name


class Works(models.Model):

    customer=models.ForeignKey(Customers, on_delete=models.CASCADE)

    description=models.TextField(max_length=300)

    amount=models.FloatField()

    