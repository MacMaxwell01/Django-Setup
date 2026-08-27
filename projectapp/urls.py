from projectapp import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("post/", views.post, name="post"),
    path("posts/", views.posts, name="posts"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/<str:pk>/", views.post, name="post"),
    path("posts/<str:pk>/edit/", views.edit_post, name="edit_post"),
    path("user/form/", views.displayform, name="userform"),
    path("user/create/", views.create_user, name="create_user"),
    path("user/custom_create/", views.custom_create_user, name="custom_create_user"),
    path("user/submit/", views.submitform, name="submitform"),
    path("students/create/", views.create_students, name="create_students"),
    path("students/<str:pk>/edit/", views.edit_student, name="edit_student"),
    path("students/<str:pk>/delete/", views.delete_student, name="delete_student"),
    path("students/", views.student_list, name="student_list"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]