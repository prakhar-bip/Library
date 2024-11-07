from django.shortcuts import *
from .models import *
import http
from django.contrib import messages

def Home(request):
    return render(request, 'Register.html')

def Register(request):
    if(request.method == "POST"):

        firstname = request.POST.get('First')
        lastname = request.POST.get('Last')
        Email = request.POST.get('email')
        Password = request.POST.get('pass')
        cnfpass = request.POST.get('cpass')
        role = request.POST.get('menu')
        
    acc = SignUp.objects.filter(email = Email , password = Password)
    if(acc.exists()):
        return HttpResponse("Account already exist. Please sign in to continue")
    else:
        Info = SignUp(roles = role , fname = firstname , lname = lastname , email = Email , password = Password , cpass = cnfpass)
        Info.save()


    if (role == 'Admin'):
        return render(request , 'Main.html')
    
    else:
        return redirect('Home_Page')

def SignIn(request):

    if (request.method == "POST"):
        Email = request.POST.get('email1')
        Password = request.POST.get('pass1')
        
        user_exist = SignUp.objects.filter(email=Email, password=Password)
        if(user_exist.exists()):
            user = user_exist.first()
            user_role = user.roles
            if(user_role == 'Admin'):
                return render(request , 'Main.html')
            
        else:
            return redirect('Home_Page')
    return render(request , 'SignIn.html')

def add(request):
    if (request.method == "POST"):
        Name = request.POST['book_name']
        Author = request.POST['Author']
        Identity = request.POST['isbn']
        Date = request.POST['date']
        Desc = request.POST['desc']
        Genretion = request.POST['genre']
        books = book(Book_title = Name , Author_name = Author , ISBN = Identity , Description = Desc , Genre = Genretion , Publish_date = Date)
        books.save()
        messages.success(request , "Book was added")

    return render(request , "Add_books.html")

def Study(request):
    return render(request , 'Main.html')

def View_books(request):
    All_books = book.objects.all()
    if (request.GET.get('search')):
        search = request.GET.get('search')
        All_books = book.objects.filter(Book_title__icontains = search)
        return render(request , 'View_books.html' , {'books':All_books})
    return render(request , 'View_books.html' , {'books':All_books})

def manage_users(request):
    Users = SignUp.objects.all()
    if (request.GET.get('search')):
        search = request.GET.get('search')
        All_Users = SignUp.objects.filter(fname__icontains = search)
        return render(request, 'Manage_users.html' , {'users' : All_Users})
    return render(request, 'Manage_users.html' , {'users' : Users})

def manage_books(request):
    issues = Issue.objects.all()
    return render(request , 'Manage_books.html' , {'Issues':issues})