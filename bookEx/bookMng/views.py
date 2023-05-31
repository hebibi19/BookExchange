from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from .models import MainMenu
from .forms import BookForm
from django.http import HttpResponseRedirect
from .models import Book
from .forms import CommentForm


from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    # print(MainMenu.objects.all())
    return render(request, 'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


def aboutUs(request):
    members = ["Brandon Hernandez", "Breck Miner", "Edson Castellanos",
               "Esther Guo", "Jacqueline Molina", "Jonathan Dang", "Mengying Chen"]

    if request.method == "GET":
        return render(request, "bookMng/about_us.html",
                      {
                          'item_list': MainMenu.objects.all(),
                          'members': members
                      }
                      )


def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                  }
                  )


def displaybooks(request):
    books = Book.objects.all()

    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                  }
                  )


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]

    # related code block for comment section
    comments = book.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # creates comment object, but doesn't save to db
            new_comment = comment_form.save(commit=False)
            try:
                new_comment.username = request.user
            except Exception:
                pass
            new_comment.book = book
            new_comment.save()

            return render(request,
                          'bookMng/book_detail.html',
                          {
                              'item_list': MainMenu.objects.all(),
                              'book': book,
                              'comments': comments,
                              'new_comment': new_comment,
                              'comment_form': comment_form,
                          }
                          )
    # if it is a GET request, initialize the form & pass it
    else:
        comment_form = CommentForm()

    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                      'comments': comments,
                      'new_comment': new_comment,
                      'comment_form': comment_form,
                  }
                  )


def mybooks(request):
    books = Book.objects.filter(username=request.user)
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return redirect('mybooks')


# method changes the Favorite attribute from False to True
def add_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    try:
        book.favorite = True
    except Exception:
        pass
    book.save()

    return redirect('mybooks')


# method displays all of the books that have the 'favorite' attribute set to True
def myfavorites(request):
    books = Book.objects.filter(favorite=True, username=request.user)

    return render(request,
                  'bookMng/myfavorites.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )


# method sets the favorite attribute from True to False
def delete_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    try:
        book.favorite = False
    except Exception:
        pass
    book.save()

    return redirect('myfavorites')


# rate book & delete rating
def rate_book(request, book_id, rating):
    book = Book.objects.get(id=book_id)
    try:
        book.rated = rating
    except Exception:
        pass
    book.save()

    return redirect('mybooks')


def delete_rating(request, book_id):
    book = Book.objects.get(id=book_id)
    try:
        book.rated = None
    except Exception:
        pass
    book.save()

    return redirect('mybooks')


def search_books(request):
    searched = request.POST['searched']
    books = Book.objects.filter(name__contains=searched)
    return render(request,
                  'bookMng/search_books.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'searched': searched,
                      'books': books,
                  }
                  )
