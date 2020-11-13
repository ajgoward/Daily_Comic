from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):

    rating = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Reviews
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-text'
