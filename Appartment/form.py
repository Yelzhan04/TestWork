from django import forms


class Sort(forms.Form):
    min_price = forms.IntegerField(label="From", required=False)
    max_price = forms.IntegerField(label="From", required=False)
    ordering = forms.ChoiceField(label='sort', required=False, choices=[
        ['price', 'from smallest'],
        ['-price', 'from bigger']
    ])
