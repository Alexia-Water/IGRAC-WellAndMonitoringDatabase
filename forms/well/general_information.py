from django import forms


class GeneralInformationForm(forms.Form):
    """
    Form of general information of well.
    """
    # identification
    id = forms.CharField()
    water_point_reference = forms.CharField()
    water_point_type = forms.CharField()

    # Location Information
    latitude = forms.FloatField(help_text='latitude of well')
    longitude = forms.FloatField(help_text='longitude of well')
    country = forms.CharField(help_text='country of well')
    address = forms.CharField(
        widget=forms.Textarea, required=False,
        help_text='country of well')
    elevation = forms.CharField(help_text='elevation of well')

    # Summary Information
    picture = forms.FileField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
