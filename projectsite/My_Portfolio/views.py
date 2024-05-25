# In views.py of your portfolio app

from django.shortcuts import render
from .models import Project  # Import any models you need

def index(request):
    # Logic for base page (if any)
    return render(request, 'My_Portfolio/index.html')
# Compare this snippet from portfolio_project/portfolio/templates/portfolio/home.html:

