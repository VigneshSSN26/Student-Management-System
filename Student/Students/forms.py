from django import forms
from .models import Student,Departments,Creditss,StaffLogin
class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = StaffLogin
        fields = ['user_id', 'password']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'user_id', 'department','password']
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # You can customize the form fields here if needed
        self.fields['password'].widget = forms.PasswordInput(render_value=False)
class CreditsForm(forms.ModelForm):
    class Meta:
        model = Creditss
        fields = ['course', 'credit_acquired', 'student']
        labels = {
            'credit_acquired': 'Mark Acquired', 
            'course':'NPTEL Course'# Change the label for 'credit_acquired'
        }