from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=50, label="Your full name: ", error_messages={
        'required': "Please enter your name"
    })
    email = forms.EmailField(label="Your email ID: ")
    review_text = forms.CharField(max_length=200, min_length=5, widget=forms.Textarea)
    rating = forms.IntegerField(max_value=5, min_value=1)