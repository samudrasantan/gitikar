from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='বিষয়')
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        msg = self.cleaned_data['message']
        num = len(msg.split())
        if num<4:
            raise forms.ValidationError("Not enough words! you have only entered %s words. please enter atleast 4 word" % num)
        return message
