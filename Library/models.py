from django.db import models


class SignUp(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=14)
    cpass = models.CharField(max_length=14)
    roles = models.CharField(max_length= 20 , default= "None")


    def __str__(self):
        return self.fname + " " + self.lname
    

class book(models.Model):

    Genre = models.CharField(max_length=20)
    Book_title = models.CharField(max_length= 200)
    Author_name = models.CharField(max_length= 200)
    ISBN = models.CharField(max_length=13, unique=True)
    Publish_date = models.DateField()
    Description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.Book_title} by {self.Author_name}"
    
class Issue(models.Model):
    name = models.CharField(max_length=150) 
    e_mail = models.EmailField()
    contact_number = models.CharField(max_length=15) 
    issue_date = models.DateField()
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.name}")