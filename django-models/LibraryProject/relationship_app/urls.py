from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    # Role-based views
    path('admin-role/', views.admin_view, name='admin-role'),
    path('librarian-role/', views.librarian_view, name='librarian-role'),
    path('member-role/', views.member_view, name='member-role'),

    # Book views (with permissions)
    path('add_book/', views.add_book_view, name='add_book'),                
    path('edit_book/<int:pk>/', views.edit_book_view, name='edit_book'),  
    path('delete_book/<int:pk>/', views.delete_book_view, name='delete_book'),
    
    # General views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]
