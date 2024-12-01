from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('El', 'ELACHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    data_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    

    def __str__(self):
        return self.name

class ChaiReview(models.Model):
    RATING_CHOICE = [
        ('1', 'Very bad'),
        ('2', 'Not good'),
        ('3', 'Good'),
        ('4', 'Very good'),
        ('5', 'Excellent')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name
    
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateField(default=timezone.now)
    valid_until = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Certificate for {self.name.chai}'


