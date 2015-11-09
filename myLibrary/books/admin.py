from django.contrib import admin 
from myLibrary.books.models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'AuthorID', 'Age', 'Country')
    search_fields = ('Name',)
    list_filter = ('Country',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'Title', 'AuthorID', 'Publisher', 'PublishDate', 'Price')
    search_fields = ('AuthorID__AuthorID',)
    list_filter = ('PublishDate','AuthorID',)
    date_hierarchy = 'PublishDate'
    #fields = ('Title', 'AuthorID', 'Publisher', 'PublishDate',)
    #raw_id_fields = ('AuthorID',)
    #filter_horizontal = ('AuthorID',) #must be a ManyToManyField.

    #ordering = ('-PublishDate',)
    
#admin.site.register(Publisher) 
admin.site.register(Author, AuthorAdmin) 
admin.site.register(Book, BookAdmin)