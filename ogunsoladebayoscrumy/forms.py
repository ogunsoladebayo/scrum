from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import User, ScrumyGoals, GoalStatus


class SignupForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter a password to use'}),
        }


class CreateGoalForm(forms.ModelForm):
    class Meta(object):
        model = ScrumyGoals
        fields = ['goal_name', 'user', 'created_by', 'owner', 'goal_status']
        widgets = {
            'goal_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter goal name'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Creator'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner'}),
            'goal_status': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreateGoalForm, self).__init__(*args, **kwargs)
        self.fields['goal_status'].label_from_instance = lambda obj: "%s" % obj.status_name
        self.fields['goal_status'].queryset = GoalStatus.objects.filter(
            status_name='Weekly Goal')
        self.fields['user'].queryset = User.objects.filter(
            username=user)


class MoveGoalForm(forms.Form):
    goal_status = forms.ModelChoiceField(GoalStatus.objects.all(), widget = forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        role = kwargs.pop('role')
        user = kwargs.pop('user')
        goal_user = kwargs.pop('goal_user')
        super(MoveGoalForm, self).__init__(*args, **kwargs)
        self.fields['goal_status'].label_from_instance = lambda obj: "%s" % obj.status_name
        if role == 'Developer':
            if  str(goal_user) == str(user):
                self.fields['goal_status'].queryset = GoalStatus.objects.filter(
                    status_name__regex=r'^(Weekly|Daily|Verify)')
            else:
                self.fields['goal_status'].disabled = True
        elif role == 'Quality Assurance':
            if  str(goal_user) == str(user):
                pass
            else:
                self.fields['goal_status'].queryset = GoalStatus.objects.filter(
                    status_name__regex=r'^(Verify|Done)')
        elif role == 'Owner':
            if  str(goal_user) == str(user):
                pass
            else:
                self.fields['goal_status'].disabled = True
        elif role == 'Admin':
            pass
