from django import forms


class ArrayForm(forms.Form):
    array_data = forms.CharField(
        widget=forms.Textarea, help_text="Enter the data elements separated by commas"
    )
    target = forms.IntegerField(help_text="Enter the target value to search for")
