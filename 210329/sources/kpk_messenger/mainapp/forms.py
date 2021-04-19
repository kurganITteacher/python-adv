from django.forms import ModelForm, HiddenInput

from mainapp.models import Message


class DialogMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('sender', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # print(field_name, field)
            if field_name == 'sender':
                field.widget = HiddenInput()
