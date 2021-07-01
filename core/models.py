from django.db import models

# Create your models here.
class Piece(models.Model):
    PAINTING = 'PA'
    ABSTRACT = 'AB'
    DRAWINGS = 'DR'
    INSTALLATIONS = 'IN'
    SCULPTURES = 'SC'
    PHOTOGRAPHY = 'PH'
    KIND = [
        (PAINTING, 'Painting'),
        (SCULPTURES, 'Sculptures'),
        (DRAWINGS, 'Drawings'),
        (ABSTRACT, 'Abstract'),
        (INSTALLATIONS, 'Installations'),
        (PHOTOGRAPHY, 'Photography'),
    ]
    image = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.TextField()
    artist = models.CharField(max_length=100)
    kind = models.CharField(
        max_length=2,
        choices=KIND,
        default=PAINTING,
    )