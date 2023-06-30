from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "publication_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price and price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_isbn(self):
        isbn = self.cleaned_data.get("isbn")
        if len(isbn) != 10 and len(isbn) != 13:
            raise forms.ValidationError(
                "ISBN must be 10 or 13 characters long."
            )
        return isbn
