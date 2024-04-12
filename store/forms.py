from django import forms


class SearchForm(forms.Form):
    SORT_CHOICES = (
        ('price_pounds', 'Sort by price (Low to high)'),
        ('-price_pounds', 'Sort by price (High to low)'),
    )

    PAGE_CHOICES = (
        (10, '10'),
        (20, '20'),
        (50, '50'),
        (100, '100'),
    )

    search_term = forms.CharField(required=True, max_length=255)
    sort_order = forms.ChoiceField(required=True, choices=SORT_CHOICES)
    page = forms.IntegerField(
        required=False, initial=1, min_value=1, max_value=9999, widget=forms.HiddenInput)
    items_per_page = forms.TypedChoiceField(
        required=True, coerce=int, choices=PAGE_CHOICES)


class CheckoutForm(forms.Form):
    full_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True, max_length=254)
    phone_number = forms.CharField(required=True, max_length=20)
    country = forms.CharField(required=True, max_length=40)
    postcode = forms.CharField(required=False, max_length=20)
    town_or_city = forms.CharField(required=True, max_length=40)
    street_address1 = forms.CharField(
        required=True, max_length=80, label="Street address 1")
    street_address2 = forms.CharField(required=False, max_length=80, label="Street address 2")
    county = forms.CharField(required=True, max_length=80)
