from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import format_html, format_html_join


class NewSchema(models.Model):
    """
    Model representing schema parameters.
    """
    schema_name = models.CharField(
        'Schema name',
        max_length=100,
        blank=False,
    )

    # COMA, DOT = ('CM', 'DT')
    COLUMN_SEPARATOR = (
        ('COMMA', 'Comma(,)'),
        ('DOT', 'Dot(.)')
    )
    column_separator = models.CharField(
        max_length=5,
        choices=COLUMN_SEPARATOR,
        default='COMMA'
    )

    STRING_CHARACTER = (
        ('ONE_QUOTE', 'One-quote(\')'),
        ('DOUBLE_QUOTE', 'Double-quote(")'),
    )
    string_character = models.CharField(
        max_length=12,
        choices=STRING_CHARACTER,
        default='DOUBLE_QUOTE'
    )


class SchemaColumn(models.Model):
    """
    Model representing types of data.
    """
    column_name = models.CharField(
        max_length=20,
        null=True,
    )
    TYPE = (
        ('JOB', 'Job'),
        ('EMAIL', 'Email'),
    )
    type = models.CharField(
        max_length=12,
        choices=TYPE,
        null=True,
    )

    first_name = models.CharField(
        'First name',
        max_length=50,
    )
    last_name = models.CharField(
        'Last name',
        max_length=50,
    )
    job = models.CharField(
        'Job',
        max_length=50,
    )
    email = models.EmailField(
        'Email',
    )
    domain_name = models.CharField(
        'Domain',
        max_length=10,
    )
    phone_number = models.CharField(
        'Phone',
        max_length=15,
    )
    company_name = models.CharField(
        'Company',
        max_length=100,
    )
    text = models.TextField()
    integer = models.IntegerField(
        default=18,
        validators=[MaxValueValidator(60), MinValueValidator(18)]
    )
    address = models.CharField(
        'Address',
        max_length=150,
    )
    date = models.DateField(
        auto_now=True,
    )

    def drop_down_list(self):
        return format_html(
            '<select size="3" multiple name="hero[]">{} {}</select>',
            self.address,
            self.date,
        )

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
