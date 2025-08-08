# User Guide for Customizable Menu System

This system allows you to create and customize a digital menu with categories and items, 
including images, fonts, colors, layout, and alignment. It uses Django as the backend with
Cloudinary for image hosting and a color picker for color customization.

---

## Models and Their Roles

### 1. MenuConfig

* Represents the overall menu configuration.
* Contains global settings such as:

  * Logo image and position (left, center, right).
  * Background image.
  * Layout (column or row).
  * Menu alignment (left or center).
  * Title text and style (font family, size, color).

### 2. Category

* Represents a category in the menu (e.g., Appetizers, Drinks).
* Belongs to a MenuConfig.
* Customizable appearance:

  * Name, font family, font size, and color.
  * Category image and its position (top or left).
  * Text alignment (left, center, right).

### 3. MenuItem

* Represents an individual item within a category.
* Customizable appearance and content:

  * Name, description, price.
  * Image and image position.
  * Font family, size, and color.

---

## Admin Interface Usage

### Access:

* Go to Django admin panel (`/admin`).

### Managing MenuConfig:

* Create or edit the single menu configuration.
* Upload a logo and background image.
* Set the layout, logo position, and menu alignment.
* Customize the title text and its font, size, and color.

### Managing Categories:

* Add/edit categories inline inside `MenuConfig` or separately via the Category admin.
* Set category name, font, size, color, and position (text alignment).
* Upload an optional image and set image position.
* Each category links to the main `MenuConfig`.

### Managing Menu Items:

* Add/edit items inline inside categories or via the MenuItem admin.
* Specify name, description, price, and appearance options.
* Upload an optional image and set image position.

---

## Frontend Behavior

* The menu is responsive and adapts for mobile devices (screens less than 768px width).
* The background image covers the whole page.
* Logo placement and menu alignment reflect the settings from admin.
* Categories and items show images and text aligned as configured.
* Font families and sizes are applied as chosen.
* Price is displayed next to the item with a dotted line separator.

---

## Customization Notes

* Fonts: A predefined list of font families is available (e.g., Roboto, Poppins, Lobster).
* Font Sizes: Choices from small (25px) to XXL (105px).
* Colors: Colors can be picked via a color picker and stored in hex format.
* Image Positions: Images can be placed either on top or to the left of the text.
* Category Position: Controls text alignment of category titles and content (left, center, right).
* Menu Alignment: Controls overall menu alignment (left or center).

