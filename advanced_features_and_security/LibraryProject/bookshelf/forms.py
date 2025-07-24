# forms.py

ExampleForm

from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(max_length=255)

<!-- templates/books/book_form.html -->

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
