from django.conf.urls.defaults import * 
from django.contrib import admin 
from myLibrary.books import views
from myLibrary.books.models import Book, Author
from django.views.generic import list_detail
#from myLibrary import views#my_homepage_view, current_datetime#, display_meta
admin.autodiscover()

book_info = {    
    'queryset': Book.objects.all(),
    'template_name': 'book_list_page.html', #tell object_list to use nalige template
    #'template_object_name': 'Book', 
    #'extra_context': {'auth_list': Author.objects.all()},
}

author_info = {
    'queryset': Author.objects.all(),
    'template_name': 'author_list_page.html',
}

urlpatterns = patterns('',
    #('^$', 'myLibrary.views.my_homepage_view'), 
    #('^time/$', 'myLibrary.views.current_datetime'),
    (r'^admin/', include(admin.site.urls)),
    #(r'^search-form/$', views.search_form),
    (r'^search/$', views.search_auth_book),
    (r'^books/$', list_detail.object_list, book_info),
    (r'^bookdetail/([^/]+)/$', views.showbook_detail),
    (r'^deletebook/([^/]+)/$', views.deletebook),
    (r'^beforeaddbook/$', views.beforeaddbook),
    (r'^addbook/$', views.addbook),
    (r'^authors/$', list_detail.object_list, author_info),
    (r'^authordetail/([^/]+)/$', views.showauthor_detail),
    (r'^deleteauthor/([^/]+)/$', views.deleteauthor),
    (r'^addauthor/$', views.addauthor),
    #(r'^addauthor/$', views.addauthor),
    #(r'^addauthor/$', views.addauthor),
    (r'^updatebook/([^/]+)/$', views.updatebook),
    #(r'^bookdetail/$', views.showbook_detail),
    #('^meta$', display_meta),
)

urlpatterns += patterns('myLibrary.views',
    ('^$', 'homepage'), 
    ('^time/$', 'current_datetime'),
)