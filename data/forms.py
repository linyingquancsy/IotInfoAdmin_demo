from django import forms

class MessageForm(forms.Form):
    title = forms.CharField(max_length=3, label='标题', min_length=2, error_messages={'min_length': '标题不符合要求'})
    email = forms.EmailField(label='邮箱')
