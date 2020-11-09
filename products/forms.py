from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('name', 'rating', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
