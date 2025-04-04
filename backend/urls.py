# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define a simple view to handle the root URL
def home(request):
    return HttpResponse("Welcome to the To-Do List API!")

urlpatterns = [
    path('', home),  # Display a welcome message at the root URL
    path('admin/', admin.site.urls),
    path('api/', include('todolist.urls')),  # Include the todolist API URLs
]
