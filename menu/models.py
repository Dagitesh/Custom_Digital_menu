from django.db import models
from colorfield.fields import ColorField
from cloudinary.models import CloudinaryField

FONT_CHOICES = [
    ("Arial", "Arial"),
    ("Helvetica", "Helvetica"),
    ("Georgia", "Georgia"),
    ("Times New Roman", "Times New Roman"),
    ("Courier New", "Courier New"),
    ("Verdana", "Verdana"),
    ("Poppins", "Poppins"),
    ("Roboto", "Roboto"),
    ("Lobster", "Lobster"),
    ("Pacifico", "Pacifico"),
    ("Vendya", "Vendya"),
    ('Caviar Dreams', 'Caviar Dreams'),
    ("Gavoline","Gavoline"),
    ("Heavitas", "Heavitas"),
    ("LemonMilk","LemonMilk"),
    ("MoonTank", "MoonTank"),
    ("Vogue", "Vogue"),
]

FONT_SIZE_CHOICES = [
    ("14px", "Small"),
    ("16px", "Normal"),
    ("20px", "Large"),
    ("24px", "Extra Large"),
]

LOGO_POSITION_CHOICES = [
    ('left', 'Left'),
    ('center', 'Center'),
    ('right', 'Right'),
]

MENU_ALIGNMENT_CHOICES = [
    ('left', 'Left'),
    ('center', 'Center'),
]

IMAGE_POSITION_CHOICES = [
    ('top', 'Top'),
    ('left', 'Left'),
]

class MenuConfig(models.Model):
    LAYOUT_CHOICES = [
        ('column', 'Column'),
        ('row', 'Row'),
    ]

    logo = CloudinaryField('logo')
    background_image = CloudinaryField('background_image')
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICES, default='column')
    logo_position = models.CharField(max_length=10, choices=LOGO_POSITION_CHOICES, default='left')
    menu_alignment = models.CharField(max_length=10, choices=MENU_ALIGNMENT_CHOICES, default='left')

    def __str__(self):
        return f"Menu Config #{self.id}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    config = models.ForeignKey(MenuConfig, on_delete=models.CASCADE, related_name='categories')
    color = ColorField(default='#000000')
    font_family = models.CharField(max_length=100, choices=FONT_CHOICES, default='Roboto')
    font_size = models.CharField(max_length=10, choices=FONT_SIZE_CHOICES, default='16px')
    image = CloudinaryField('category_image', blank=True, null=True)
    image_position = models.CharField(max_length=10, choices=IMAGE_POSITION_CHOICES, default='top')

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('menu_item_image', blank=True, null=True)
    image_position = models.CharField(max_length=10, choices=IMAGE_POSITION_CHOICES, default='top')
    font_family = models.CharField(max_length=100, choices=FONT_CHOICES, default='Roboto')
    font_size = models.CharField(max_length=10, choices=FONT_SIZE_CHOICES, default='16px')
    color = ColorField(default='#000000')

    def __str__(self):
        return self.name
