#coding=utf-8
#URLS for Coltrane app

from coltrane.models import Entry, Category
from coltrane.views import CategoryDetailView

from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.conf import settings

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/{0,1}$', YearArchiveView.as_view(model=Entry, date_field="pub_date", make_object_list = True), name='coltrane_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/{0,1}$', MonthArchiveView.as_view(model=Entry, date_field="pub_date", month_format="%m"), name='coltrane_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/{0,1}$', DayArchiveView.as_view(model=Entry, date_field="pub_date", month_format="%m"), name='coltrane_entry_archive_day'),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/{0,1}$', DateDetailView.as_view(model=Entry, date_field="pub_date", month_format="%m"), name='coltrane_entry_detail'),
)
urlpatterns += patterns('',
    url(r'^categories/{0,1}', ListView.as_view(model=Category), name='coltrane_category_list'),
    url(r'^categories/(?P<slug>[-\w]+)/{0,1}$', CategoryDetailView.as_view(), name="coltrane_category_detail"),
    url(r'/{0,1}$', 'coltrane.views.category_list'), 
)
