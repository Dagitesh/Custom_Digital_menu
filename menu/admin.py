from django.contrib import admin
from .models import MenuConfig, Category, MenuItem

# Inline for MenuItem inside Category
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


# Admin for Category showing MenuItems inline
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ("name", "config", "position", "font_size", "font_family", "color")
    list_filter = ("config", "position", "font_size", "font_family")
    search_fields = ("name",)

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "config")
        }),
        ("Appearance", {
            "fields": ("color", "font_family", "font_size", "position")
        }),
        ("Image Settings", {
            "fields": ("image", "image_position")
        }),
    )


# Inline for Category inside MenuConfig
class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1
    show_change_link = True


# Admin for MenuConfig showing Categories inline
@admin.register(MenuConfig)
class MenuConfigAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ("id", "layout", "logo_position", "menu_alignment", "title_text", "title_font_size")
    list_filter = ("layout", "logo_position", "menu_alignment")
    search_fields = ("title_text",)

    fieldsets = (
        ("Layout & Branding", {
            "fields": ("layout", "logo", "logo_position", "background_image", "menu_alignment")
        }),
        ("Title Appearance", {
            "fields": ("title_text", "title_font_family", "title_font_size", "title_color")
        }),
    )

    def has_add_permission(self, request):
        # Prevent adding more than one MenuConfig
        return not MenuConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Optional: prevent deletion too
        return False


# Register MenuItem separately
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "font_size", "font_family", "color")
    list_filter = ("category", "font_size", "font_family")
    search_fields = ("name", "description")

    fieldsets = (
        ("Basic Info", {
            "fields": ("category", "name", "description", "price")
        }),
        ("Appearance", {
            "fields": ("color", "font_family", "font_size")
        }),
        ("Image Settings", {
            "fields": ("image", "image_position")
        }),
    )
