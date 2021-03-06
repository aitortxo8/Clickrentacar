from django import forms
from vehicles.models import Vehicle, VechiclePublication


class VehicleRegisterForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['carRegistration', 'brand', 'carModel', 'year', 'seatsNumber']
        widgets = {
            'carRegistration': forms.TextInput(
                attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '15'}),
            'brand': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '15'}),
            'carModel': forms.TextInput(
                attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '15'}),
            'year': forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '15'}),
            'seatsNumber': forms.NumberInput(
                attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '15'})
        }

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


class VehiclePublicationForm(forms.ModelForm):
    class Meta:
        model = VechiclePublication
        fields = ['price', 'description', 'published']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '15'}),
            'description': forms.TextInput( attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '100'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nick'}),
        }

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
