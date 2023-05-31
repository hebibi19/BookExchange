from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    # aboutUS URL path
    path('aboutus', views.aboutUs, name='aboutus'),
    # three URL paths needed for Favorites Page
    path('add_favorite/<int:book_id>', views.add_favorite, name='add_favorite'),
    path('delete_favorite/<int:book_id>', views.delete_favorite, name='delete_favorite'),
    path('myfavorites', views.myfavorites, name='myfavorites'),
    # edit rating
    path('rate_book/<int:book_id>/<int:rating>', views.rate_book, name='rate_book'),
    path('delete_rating/<int:book_id>', views.delete_rating, name='delete_rating'),
    #search path
    path('search_books', views.search_books, name='search-books'),
]


