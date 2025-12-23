from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
        name = models.CharField(max_length=100)
        code = models.CharField(max_length=10)

        def __str__(self):
            return self.name


class Address(models.Model):
        street = models.CharField(max_length=255)
        city = models.CharField(max_length=100)
        state = models.CharField(max_length=100)
        zip_code = models.CharField(max_length=20)
        country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.street}, {self.city}, {self.state}, {self.zip_code}, {self.country}"



class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def full_name(self):
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class BookOutlet(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(null=True, max_length=255)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # Additional fields can be added as needed
    published_contries = models.ManyToManyField(Country, blank=True)
    address = models.ManyToManyField(Address, blank=True)

    #
   # author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    # is_bestseller = models.BooleanField(default=False)
    # location = models.CharField(max_length=255)
    # established_date = models.DateField()
    # is_active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)




    def get_absolute_url(self):
        return reverse("book_details", args={self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BookOutlet, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} - {self.name} - {self.title} - {self.rating}"


    def get_countries(self):
        return ", ".join(c.name for c in self.published_contries.all())

    def get_addresses(self):
        return ", ".join(a.street for a in self.address.all())
