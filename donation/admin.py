from django.contrib import admin
from homepage.models import donatemoney,donatevaluables

# Register your models here.

admin.site.register((donatemoney,donatevaluables))
