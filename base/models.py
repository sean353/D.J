from django.db import models






# Create your models here.
class Book(models.Model):
    Book_name = models.CharField(max_length=50,null=True,blank=True)
    Autor = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['Book_name','Autor']
 
    def __str__(self):
           return self.Book_name
    


class Customer(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email= models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['name','email']
 
    def __str__(self):
           return self.name


