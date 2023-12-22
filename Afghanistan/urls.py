from django.contrib import admin
from django.urls import path

from . import views
from .views import afghanistan_overview, history, diplomacy, culture, form_submission
from .views import output_all_entries, contact, map
app_name = 'Afghanistan'
urlpatterns = [
    path('', afghanistan_overview, name='afghanistan_overview'),
    path('Afghanistan/', afghanistan_overview, name='afghanistan_overview'),
    path("Afghanistan/admin/", admin.site.urls),
    path('Afghanistan/history/', history, name='history'),
    path('Afghanistan/diplomacy/', diplomacy, name='diplomacy'),
    path('Afghanistan/culture/', culture, name='culture'),
    path('Afghanistan/message/', output_all_entries, name='message'),
    path('Afghanistan/contact/', contact, name='contact'),
    path('Afghanistan/map/', map, name='map'),
    path('process_form', views.process_form, name='process_form'),
    path('submit', form_submission, name='form_submission'),
]
