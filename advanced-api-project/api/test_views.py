from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='pass123')
        # Create an author
        self.author = Author.objects.create(name='George Orwell')
        # Create some books
        self.book1 = Book.objects.create(title='1984', publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title='Animal Farm', publication_year=1945, author=self.author)
        
        # APIClient instance
        self.client = APIClient()

    def test_list_books(self):
        """Test listing all books (unauthenticated access)"""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_search_books(self):
        """Test search by title"""
        url = reverse('book-list') + '?search=1984'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_order_books(self):
        """Test ordering by publication_year descending"""
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the first book has the newest publication_year
        self.assertEqual(response.data[0]['publication_year'], 1949)

    def test_create_book_authenticated(self):
        """Test creating a book as authenticated user"""
        self.client.login(username='testuser', password='pass123')
        url = reverse('book-create')
        data = {
            'title': 'Homage to Catalonia',
            'publication_year': 1938,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='Homage to Catalonia').publication_year, 1938)

    def test_create_book_unauthenticated(self):
        """Test creating a book as unauthenticated user should fail"""
        url = reverse('book-create')
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2025,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test updating a book as authenticated user"""
        self.client.login(username='testuser', password='pass123')
        url = reverse('book-update', args=[self.book1.id])
        data = {
            'title': '1984 (Updated)',
            'publication_year': 1950,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, '1984 (Updated)')
        self.assertEqual(self.book1.publication_year, 1950)

    def test_delete_book_authenticated(self):
        """Test deleting a book as authenticated user"""
        self.client.login(username='testuser', password='pass123')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        """Test deleting a book as unauthenticated user should fail"""
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
