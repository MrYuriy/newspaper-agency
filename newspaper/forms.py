from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Redactor, Newspaper, Topic
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


class RedactorCreationForm(UserCreationForm):
    max_year_experience = 30

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MaxValueValidator(max_year_experience)]
    )

    class Meta(UserCreationForm):
        model = Redactor
        fields = fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def validate_max_year_experience(self):
        if self.max_year_experience > 30:
            raise ValidationError('Max year experience should not exceed 30 years')


class NewspaperCreationUpdateForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "topic", "publishers"]


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )
