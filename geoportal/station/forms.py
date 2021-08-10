from django import forms
from django.forms.models import inlineformset_factory
from station.models import Station, StationType, Basin, MSC


class StationTypeForm(forms.ModelForm):

    class Meta:
        model = StationType
        fields = ['station_type', 'description']


class BasinForm(forms.ModelForm):

    class Meta:
        model = Basin
        fields = ['basin_name']


class MSCForm(forms.ModelForm):

    class Meta:
        model = MSC
        fields = ['msc_name']

class StationForm(forms.ModelForm):

    class Meta:

        model = Station
        fields = [
            "station_id",
            "begin_date",
            "end_date",
            "name",
            "region",
            "zone",
            "woreda",
            "basin",
            "station_type",
            "msc",
            "geography_1",
            "longitude",
            "geography_2",
            "latitude",
            "elevation",
            "note"
        ]
