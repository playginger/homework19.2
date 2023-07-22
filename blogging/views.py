from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from blogging.models import Blogging


class BloggingListView(ListView):
    model = Blogging
    #template_name = 'blogging/blogging_list.html'
    #context_object_name = 'blogging_list'

    def get_queryset(self):
        return super().get_queryset().filter(publications=True)


class BloggingCreateView(CreateView):
    model = Blogging
    fields = ['header', 'content']
    success_url = reverse_lazy('blogging:list')

    #def form_valid(self, form):
    #    form.instance.slug = slugify(form.instance.header)
    #    return super().form_valid(form)


class BloggingDetailView(DetailView):
    model = Blogging
    template_name = 'blogging/blogging_detail.html'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.view_count += 1
        self.object.save()
        return super().get(request, *args, **kwargs)


class BloggingUpdateView(UpdateView):
    model = Blogging
    fields = ['header', 'content']

    def get_success_url(self):
        return reverse('blogging_detail', kwargs={'pk': self.object.pk})


class BloggingDeleteView(DeleteView):
    model = Blogging
    template_name = 'blogging/blogging_delete.html'
