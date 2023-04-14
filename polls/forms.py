from django import forms
from .models import Poll, Choice


class PollAddForm(forms.ModelForm):
    """
    Form for adding a new poll with choices.

    This form is used to add a new poll with choices. It inherits from
    `forms.ModelForm` and defines additional form fields and widgets for
    the 'text', 'choice1', and 'choice2' fields of the 'Poll' model.

    """

    choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Poll
        fields = ['text', 'choice1', 'choice2']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class EditPollForm(forms.ModelForm):
    """
    Form for editing an existing poll.

    This form is used to edit an existing poll. It inherits from `forms.ModelForm`
    and defines additional form fields and widgets for the 'text' field of the 'Poll'
    model.

    """
    class Meta:
        model = Poll
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class ChoiceAddForm(forms.ModelForm):
    """
    Form for adding a new choice to a poll.

    This form is used to add a new choice to a poll. It inherits from `forms.ModelForm`
    and defines additional form fields and widgets for the 'choice_text' field of the 'Choice'
    model.

    """
    class Meta:
        model = Choice
        fields = ['choice_text', ]
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control', })
        }
