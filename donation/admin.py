from django.contrib import admin
from .models import donatemoney,donatevaluables

# Register your models here.

admin.site.register((donatemoney,donatevaluables))
