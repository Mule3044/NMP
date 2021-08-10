from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
from station.models import Station, StationType, Basin, MSC
import pg8000
from station.forms import StationForm


# Create your views here.
def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station/station_list.html', {'stations': stations})


# class CreateStationView(SuccessMessageMixin, CreateView):
#     model = Station
#     fields = '__all__'
#     success_message = "New station successfully added."

#     def get_form(self):
#         form = super(CreateStationView, self).get_form()
#         form.fields['begin_date'].widget = widgets.DateInput(
#             attrs={'type': 'date'})
#         form.fields['end_date'].widget = widgets.DateInput(
#             attrs={'type': 'date'})
#         return form


class UpdateStationView(SuccessMessageMixin, UpdateView):
    model = Station
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        form = super(UpdateStationView, self).get_form()
        return form


class DeleteStationView(DeleteView):
    model = Station
    success_url = reverse_lazy('station:station-list')


class StationDetailView(DetailView):
    model = Station
    template_name = "station/station_detail.html"


# class StationListView(ListView):
#     model = Station
#     template_name = 'station/station_list.html'
def create_Station(request):
    conn = pg8000.connect(database="IncidentManagmentDb",
                          user="postgres", password="postgres")
    cursor = conn.cursor()
    cursor.execute("Select woreda,gid from nfs_woredas")
    results = cursor.fetchall()
    woreda_List = []

    for row in results:
        woreda, gid = row
        slDict = {}
        slDict['woreda'] = woreda
        slDict['gid'] = gid

        woreda_List.append(slDict)

    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            station = form.save(commit=False)
            station.save()
    else:
        form = StationForm()

    stationTypeList = StationType.objects.all().values('id', 'station_type')
    basinList = Basin.objects.all().values('id', 'basin_name')
    mscList = MSC.objects.all().values('id', 'msc_name')

    context = {
        "form": form,
        "basinList": basinList,
        "mscList": mscList,
        "stationTypeList": stationTypeList,
        "woreda_List": woreda_List
    }
    return render(request, 'station/create_station.html', context)
