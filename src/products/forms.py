from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField(
                        label='',
                        widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Please enter a title"
                                }
                            )
                        )
    description = forms.CharField(
                        required=True,
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Please enter a description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    "cols": 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=0.00)
