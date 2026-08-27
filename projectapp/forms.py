from django import forms
from projectapp.models import Post, Student


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }