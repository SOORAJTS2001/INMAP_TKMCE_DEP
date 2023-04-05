from .models import MyModel
from django.forms import ModelForm
class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['From', 'To']