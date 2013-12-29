#coding=utf-8
from django.shortcuts import render_to_response
from coltrane.models import Entry

def entries_index(request):
    return render_to_response('coltrane/index.html', {'entry_list' : Entry.objects.all()})

def entry_detail(request, year, month, day, slug):
    import datetime, time
    date_stamp = time.strptime(year+"/"+month+"/"+day, "%Y/%m/%d")
    pub_date = datetime.date(*date_stamp[:3])
    return render_to_response('coltrane/entry_detail.html',
                              {'entry' : Entry.objects.get(pub_date__year=pub_date.year, pub_date__month=pub_date.month, pub_date__day=pub_date.day, slug=slug)})
