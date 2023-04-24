from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Redactor, Newspaper, Topic


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)


class NewspaperCreationUpdateForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "topic", "publishers"]
