from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=300)
    stage = models.ForeignKey(
        'Stage',
        on_delete = models.SET_DEFAULT,
        default = 'prep',
        to_field = 'name',
    )
    due_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    context = models.ForeignKey(
        'Context',
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )
    project = models.ForeignKey(
        'Project',
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )
    delegated_to = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.description
    
    def defer(self):
        self.stage = 'defer'
        self.save()

    def delegate(self):
        self.stage = 'delegate'
        
        ## ADD PROMPT FOR delegated_to FIELD
        self.save()

class Stage(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    IMMEDIATE = 'IM'
    SHORTTERM = 'ST'
    MEDTERM = 'MT'
    LONGTERM = 'LT'

    term_choices = (
        (IMMEDIATE, 'Immediate'),
        (SHORTTERM, '1-2 Years'),
        (MEDTERM, '3-5 Years'),
        (LONGTERM, '6+ Years'),
    )

    term = models.CharField(
        max_length = 2,
        choices = term_choices,
        default = IMMEDIATE,
    )

class Project(models.Model):

    name = models.CharField(max_length=300)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def add_task():
        pass

class Context(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=300, blank=True, null=True)
    phone_regex = RegexValidator(
        regex = r'^\(\d{3}\) \d{3}\-\d{4}$',
        message = 'Phone number must be in the format (999) 999-9999.'
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=14, blank=True, null=True)
