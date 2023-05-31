from django.contrib import admin
from .models import MainMenu
from .models import Book
from .models import Comment

# Register your models here.


admin.site.register(MainMenu)
admin.site.register(Book)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'body', 'book', 'created_on', 'up_votes', 'active')
    list_filter = ('active', 'created_on', 'up_votes')
    search_fields = ('username', 'body')
    actions = ['approve_comments', 'unapprove_comments', 'reset_up_vote']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    def unapprove_comments(self, request, queryset):
        queryset.update(active=False)

    def reset_up_vote(self, request, queryset):
        queryset.update(up_votes=0)
