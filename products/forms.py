from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):

    rating = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Reviews
        fields = ('__all__')
