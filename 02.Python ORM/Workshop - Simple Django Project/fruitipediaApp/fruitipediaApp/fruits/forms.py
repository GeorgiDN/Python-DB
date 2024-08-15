from django import forms
from fruitipediaApp.fruits.models import Category, Fruit


class CategoryBaseForm(forms.ModelForm):
    # Name (background) for field - help text

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Category name'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''  # remove label over field


class CategoryAddForm(CategoryBaseForm):
    pass


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit name', }),
            'description': forms.TextInput(attrs={'placeholder': 'Enter the description'}),
            'nutrition': forms.NumberInput(attrs={'placeholder': 'Enter the fruit nutrition'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter the url for the image'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class AddFruitForm(BaseFruitForm):
    pass


class EditFruitFrom(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
