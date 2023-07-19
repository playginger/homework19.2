from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from blogging.models import Blogging


class BloggingListView(ListView):
    model = Blogging
    template_name = 'blogging/blogging_list.html'
    context_object_name = 'blogging_list'


class BloggingCreateView(CreateView):
    model = Blogging
    fields = ['header', 'content']


class BloggingDetailView(DetailView):
    model = Blogging
    template_name = 'blogging/blogging_detail.html'


class BloggingUpdateView(UpdateView):
    model = Blogging
    fields = ['header', 'content']


class BloggingDeleteView(DeleteView):
    model = Blogging
    template_name = 'blogging/blogging_delete.html'
