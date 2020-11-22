from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Schema(models.Model):
    """
    Model representing schema parameters.
    """
    schema_name = models.TextField(
        'Schema name',
        max_length=50,
        blank=False,
    )

    # COMA, DOT = ('CM', 'DT')
    COLUMN_SEPARATOR = (
        ('COMMA', 'Comma(,)'),
        ('DOT', 'Dot(.)')
    )
    column_separator = models.CharField(
        max_length=7,
        choices=COLUMN_SEPARATOR,
        default='COMMA'
    )

    STRING_CHARACTER = (
        ('ONE_QUOTE', 'One-quote(\')'),
        ('DOUBLE_QUOTE', 'Double-quote(")'),
    )
    string_character = models.CharField(
        max_length=15,
        choices=STRING_CHARACTER,
        default='DOUBLE_QUOTE'
    )


class DataType(models.Model):
    """
    Model representing types of data.
    """
    first_name = models.TextField(
        'First name',
        max_length=250,
        help_text='Name',
    )
    last_name = models.TextField(
        'Last name',
        max_length=250,
        help_text='Name',
    )
    job = models.CharField(
        'Job',
        max_length=250,
        help_text='Job role',
    )
    email = models.EmailField(
        'Email',
        help_text='Email',
    )
    domain_name = models.CharField(
        'Domain',
        max_length=10,
        help_text='Domain',
    )
    phone_number = models.CharField(
        'Phone',
        max_length=15,
        help_text='Phone number',
    )
    company_name = models.CharField(
        'Company',
        max_length=250,
        help_text='Company',
    )
    text = models.TextField()
    integer = models.IntegerField(
        default=18,
        validators=[MaxValueValidator(18), MinValueValidator(60)]
    )
    address = models.CharField(
        'Address',
        max_length=250,
        help_text='Address',
    )
    date = models.DateField()

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]
