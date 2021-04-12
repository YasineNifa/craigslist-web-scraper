from django.contrib import admin

# Register your models here.
# to use the migration, we must add this
from .models import Search
admin.site.register(Search)
