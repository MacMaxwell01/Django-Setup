from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from projectapp.models import Post, Student
from projectapp.forms import PostForm, StudentForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.
 


def home(request):
    return render(request, "index.html")


def about(request):
    about_message = "This is a message for the about page from the backend"

    best_players = ["Messi", "Ronaldo", "Neymar", "Mbappe"]
    GOAT = "CR7"

    context = {
        "taofeek": about_message,
        "programmer_name": "CR9",
        "age": 23,
        "best_players": best_players,
        "GOAT": GOAT,
    }
    print(context)

    return render(request, "about.html", context)


def profile(request):
    me = {"name": "Awele", "class": "Python", "age": 23}

    return JsonResponse(me)


def posts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts.html", context)

def post(request, pk):
    # the_post = Post.objects.get(pk=pk)
    the_post = get_object_or_404(Post,pk=pk)
    context = {"post": the_post}
    return render(request, "post.html", context)

def displayform(request):
    return render(request, "userform.html")

def submitform(request):
    if request.method == "POST":
        lastname = request.POST.get("lastname")
        firstname = request.POST.get("firstname") 
        email = request.POST.get("email")
        department = request.POST.get("department")
        matricnumber = request.POST.get("matricnumber")

        values = {"lastname": lastname, "firstname": firstname, "email": email, "department": department, "matricnumber": matricnumber}
        return JsonResponse(values)
    
    return redirect("userform")

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm()

    context ={"post_form":form}
    return render(request, "post_form.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("post", pk=post.pk)

    else:
        form = PostForm(instance=post)

    context ={"post_form":form}
    return render(request, "post_form.html", context)

def create_user(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created Successfully!😁")
    else:
        form = UserCreationForm()
   
    context = {"form": form}
    return render(request, "create_user.html", context)

def custom_create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("ConfirmPassword")

        # Check if all fields are filled
        if not (username and email and password and confirm_password):
            messages.error(request, "Please fill in all fields!😡")
            return redirect("custom_create_user")

        is_valid = True
        # Check if username already exists
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username already exists!😡")
            is_valid = False

        # Check if email already exists
        if User.objects.filter(email__iexact=email).exists():
            messages.error(request, "Email already exists!😡")
            is_valid = False

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!😡")
            is_valid = False

        # If any validation failed
        if not is_valid:
            return redirect("custom_create_user")

        # Create the user
        created_user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            f"Hi {created_user.username}! Your account has been created successfully!😁"
        )

        return redirect("login")  # Redirect to the login page after successful registration

    # Handles GET requests
    return render(request, "custom_create_user.html")



def create_students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f"Student {student.firstname} added successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "student_form.html", {"student_form": form, "form_title": "Add student"})

def student_list(request):
    students = Student.objects.all()

    context = {"students": students}
    return render(request, "students/students-table.html", context)


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    context = {"student_form": form}
    return render(request, "student_form.html", context)


@login_required(login_url='login')
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    context = {"student_form": form, "form_title": "Edit student"}
    return render(request, "student_form.html", context)


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("student_list")

    context = {"student": student}
    return render(request, "students/student_confirm_delete.html", context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password.')
            return redirect("login")  # Redirect back to the login page.
        
        auth.login(request, user)
        return redirect("home")  # Redirect to a success page.
    return render(request, 'auth/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')  # Redirect to a success page after logout.   
    

    