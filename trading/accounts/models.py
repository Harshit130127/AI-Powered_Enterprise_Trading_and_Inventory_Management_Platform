from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    """ we are using custom users here,
    to edit according to our demand"""


    email = models.EmailField(unique=True)  # unique=True creates an index automatically
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        """
        why i choose meta?
        ans. because by using meta i can have custom ordering and indexing for my model
        that would reduce the time complexity of my queries and make it more efficient
        ( because for efficeincy it would create a b-tree index in the postgresql database)

        """
        ordering = ["-date_joined"]  # newest users first (API usability)
        indexes = [
            models.Index(fields=["phone_number"]),  # to search by phone or to increase efficency

        ]


    def __str__(self):
        return self.email or self.username

