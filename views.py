#coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.detail import DetailView
from coltrane.models import Entry, Category

def entries_index(request):
    return render_to_response('coltrane/index.html', {'entry_list' : Entry.objects.all()})

#def entry_detail(request, year, month, day, slug):
#    import datetime, time
#    date_stamp = time.strptime(year+"/"+month+"/"+day, "%Y/%m/%d")
#    pub_date = datetime.date(*date_stamp[:3])
#    return render_to_response('coltrane/entry_detail.html',
#                              {'entry' : Entry.objects.get(pub_date__year=pub_date.year, pub_date__month=pub_date.month, pub_date__day=pub_date.day, slug=slug)})

def category_list(request):
    return render_to_response('coltrane/category_list.html',
                              {'object_list': Category.objects.all()}
                              )

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('coltrane/category_detail.html',
                              {'object_list': category.entry_set.all(), 'category': category})

class CategoryDetailView(DetailView):
    model=Category
    def get_context_data(self, **kwargs):
        context=super(CategoryDetailView, self).get_context_data(**kwargs)
        return context