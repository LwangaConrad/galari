from django import forms
from .models import Piece

class PieceForm(forms.ModelForm):
    description = forms.CharField(
        required = False,
        widget = forms.Textarea(
            attrs = {
                "placeholder": "Describe the artpiece",
                "rows": 10,
                "cols": 120
            }
        )
    )
    class Meta:
        model = Piece
        fields = [
            'image',
            'title',
            'description', 
            'price',
            'artist',
            'kind'
        ]
    # def clean_price(self, *args, **kwargs):
    #     price = self.cleaned_data.get("price")
    #     if price < 1000000:
    #         return price
    #     else:
    #         raise forms.ValidationError("perhaps you should reevaluate the price in dollars")
