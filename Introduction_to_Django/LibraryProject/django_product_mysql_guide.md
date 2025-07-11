# Django Product Model with MySQL Integration

This guide walks you through:

- Creating a `Product` model in Django
- Performing CRUD operations using Django ORM
- Filtering and ordering products
- Configuring MySQL as your database
- Running migrations
- Installing MySQL driver

---

## 1. Create the `Product` Model

In your app's `models.py` (e.g., in `store/models.py`):

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```

---

## 2. CRUD Operations Using Django ORM

Open the Django shell:

```bash
python manage.py shell
```

**Create a Product:**

```python
from store.models import Product
product = Product.objects.create(name="Laptop", description="Gaming laptop", price=1200.00, category="Electronics")
```

**Retrieve a Product:**

```python
product = Product.objects.get(id=1)
print(product.name)
```

**Update a Product:**

```python
product.price = 1100.00
product.save()
```

**Delete a Product:**

```python
product.delete()
```

---

## 3. Query: Filter and Order Products

**Filter by Category:**

```python
electronics = Product.objects.filter(category="Electronics")
```

**Order by Price (Ascending):**

```python
sorted_products = Product.objects.order_by('price')
```

**Order by Price (Descending):**

```python
sorted_desc = Product.objects.order_by('-price')
```

---

## 4. Configure MySQL Database in `settings.py`

Update your Django project’s `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> ⚠️ Make sure the database `your_database_name` already exists in your MySQL server.

---

## 5. Install MySQL Driver

Install `mysqlclient`:

```bash
pip install mysqlclient
```

---

## 6. Run Migrations

Run the following commands to create the database tables:

```bash
# Create migration files
python manage.py makemigrations store

# Apply migrations
python manage.py migrate
```

---

## ✅ Done!

You now have a working Django `Product` model connected to a MySQL database with full CRUD support and custom queries.
