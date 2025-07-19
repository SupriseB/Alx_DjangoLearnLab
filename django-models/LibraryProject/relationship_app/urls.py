
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  
    path('admin-role/', admin_view.admin_view, name='admin-role'),
    path('librarian-role/', librarian_view.librarian_view, name='librarian-role'),
    path('member-role/', member_view.member_view, name='member-role')
    
    # Other views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]

