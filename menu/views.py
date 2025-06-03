from django.shortcuts import render
from .models import MenuConfig

def menu_view(request):
    menu_config = MenuConfig.objects.first()  # or filter by cafe ID
    return render(request, 'menu/menu.html', {'config': menu_config})
