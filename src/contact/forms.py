from crispy_forms.helper import FormHelper
from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=False, max_length=50)
    email_address = forms.EmailField(max_length=150, required=True)
    subject = forms.CharField(required=False, max_length=50)
    message = forms.CharField(required=True, widget=forms.Textarea, max_length=2000)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields["first_name"].widget.attrs["placeholder"] = "Rachel"
        self.fields["last_name"].widget.attrs["placeholder"] = "Smith"
        self.fields["email_address"].widget.attrs["placeholder"] = "name@example.com"
        self.fields["subject"].widget.attrs["placeholder"] = "COMPSCI Research Topics"
        self.fields["message"].widget.attrs[
            "placeholder"
        ] = "Kia Ora, I was wondering if I could find out more about the kind of research that takes place at the University of Auckland?"  # noqa: E501
