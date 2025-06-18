from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    video = models.FileField(upload_to='product_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True) 
    
    # oop
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to='product_images/')

    def __str__(self):
        return f"Image of {self.product.name}"
