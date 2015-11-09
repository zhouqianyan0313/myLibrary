# Create your views here.
from django.shortcuts import render_to_response
#from django.http import HttpResponse
from django.template import Context

from myLibrary.books.models import Book, Author

def search_form(request):    
    return render_to_response('search_form.html')

def search_auth_book(request):   
    errors = []   
    if 'q' in request.GET:        
        q = request.GET['q']        
        if not q:            
            errors.append('It\'s empty! Enter an author name.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else: 
            id_auth = Author.objects.filter(Name__icontains=q)
            books = Book.objects.filter(AuthorID__icontains=id_auth)       
            return render_to_response('searchbook_results.html', {'books': books, 'query': q})
    return render_to_response('searchbook_form.html', {'errors': errors})

def showbook_detail(request, q):
    bk = Book.objects.get(Title__icontains=q)# not use filter
    auth = Author.objects.get(AuthorID__icontains=bk.AuthorID)
    authid = auth.AuthorID
    return render_to_response('show_book_detail.html', {'book': bk, 'auth': auth, 'authid': authid})

def showauthor_detail(request, q):
    au = Author.objects.get(Name=q)# not use filter
    return render_to_response('show_author_detail.html', {'auth': au})

def beforeaddbook(request):
    return render_to_response('beforeaddbook.html') 
    
def addbook(request):
    if request.method == 'POST':
        post = request.POST
        auid = Author.objects.get(AuthorID__icontains=post['AuthorID'])
        new_book = Book(
            ISBN = post["ISBN"],
            Title = post["Title"],
            AuthorID = auid,#post["AuthorID"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"],) 
        new_book.save()
    auth = Author.objects.all()
    return render_to_response('addbook.html', {'auth': auth})    

def addauthor(request):
    if request.method == 'POST':
        post = request.POST
        new_auth = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"],) 
        new_auth.save()
    return render_to_response('addauthor.html') 

def deletebook(request, d):
    #id = request.GET["id"]
    bk = Book.objects.get(Title__icontains=d)
    bkname = bk.Title
    au = Author.objects.get(AuthorID = bk.AuthorID)
    auname = au.Name
    bk.delete()
    au.delete()
    return render_to_response("delete.html", {'bkname': bkname, 'auname': auname})   

def deleteauthor(request, d):
    au = Author.objects.get(Name__icontains=d)
    auname = au.Name
    bk = Book.objects.get(AuthorID=au)
    bkname = bk.Title
    au.delete()
    bk.delete()
    return render_to_response("delete.html", {'bkname': bkname, 'auname': auname})  
    
def updatebook(request, q):
    bk = Book.objects.get(Title=q)
    au = bk.AuthorID
    if request.method == 'POST':
        post = request.POST
        au.Name = post["Name"]
        au.Age= post["Age"]
        au.Country = post["Country"]
        bk.Publisher = post["Publisher"]
        bk.PublishDate = post["PublishDate"]
        bk.Price = post["Price"]
        bk.save()
        au.save()
    return render_to_response("update.html", {'bk': bk, 'au': au})
    
    
    
    
    