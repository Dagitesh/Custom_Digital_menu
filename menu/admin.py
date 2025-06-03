from django.contrib import admin
from .models import MenuConfig, Category, MenuItem

# Inline for MenuItem inside Category
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

# Admin for Category showing MenuItems inline
class CategoryAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

# Inline for Category inside MenuConfig
class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1
    show_change_link = True

# Admin for MenuConfig showing Categories inline
@admin.register(MenuConfig)
class MenuConfigAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

    def has_add_permission(self, request):
        # Prevent adding more than one MenuConfig
        return not MenuConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Optional: prevent deletion too
        return False

# Register Category separately to access MenuItems
admin.site.register(Category, CategoryAdmin)
