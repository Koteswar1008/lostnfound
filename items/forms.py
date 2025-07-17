from django import forms
from .models import LostFoundItem

class LostFoundItemForm(forms.ModelForm):
    latitude = forms.FloatField(
        required=True,
        widget=forms.HiddenInput(attrs={'id': 'id_latitude'}),
    )
    longitude = forms.FloatField(
        required=True,
        widget=forms.HiddenInput(attrs={'id': 'id_longitude'}),
    )

    class Meta:
        model = LostFoundItem
        exclude = ['posted_by', 'is_verified', 'date_reported']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter location description (e.g., "Near Main Library")'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['latitude'].initial = self.instance.latitude
            self.fields['longitude'].initial = self.instance.longitude