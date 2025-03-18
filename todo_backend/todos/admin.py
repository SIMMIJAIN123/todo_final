from django.contrib import admin
from .models import Todo  # Import the model

# Register the model to make it visible in the admin panel
admin.site.register(Todo)
