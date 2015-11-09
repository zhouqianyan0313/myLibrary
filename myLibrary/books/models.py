from django.db import models

# Create your models here.
'''class Publisher(models.Model):    
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)    
    city = models.CharField(max_length=60)    
    state_province = models.CharField(max_length=30)    
    country = models.CharField(max_length=50)   
    website = models.URLField(blank=True)
    
    def __unicode__(self):       
        return self.name
        
    class Meta:
        ordering = ['name']'''

class Author(models.Model):  
    AuthorID = models.CharField(max_length=10)
    Name = models.CharField(max_length=30)
    Age = models.IntegerField(max_length=3)  
    Country = models.CharField(max_length=30)    
    #email = models.EmailField()
    class Meta:
        ordering = ['Name']
    
    def __unicode__(self):
        return u'%s' % self.AuthorID# %s %d %s' % (self.Name, self.AuthorID, self.Age, self.Country)

class Book(models.Model):  
    ISBN = models.CharField(primary_key=True, max_length=30)
    Title = models.CharField(max_length=50)
    AuthorID = models.ForeignKey(Author)   
    #authors = models.ManyToManyField(Author)    
    Publisher = models.CharField(max_length=30)    
    PublishDate = models.DateField()
    Price = models.DecimalField(max_digits=10, decimal_places=6)
    
    def __unicode__(self):
        return u'%s %s %s %s %s %d' % (self.ISBN, self.Title, self.AuthorID, self.Publisher, self.PublishDate, self.Price)
        
    class Meta:
        ordering = ['Title']
    