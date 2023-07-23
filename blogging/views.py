from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from blogging.models import Blogging


class BloggingListView(ListView):
    model = Blogging

    # template_name = 'blogging/blogging_list.html'
    # context_object_name = 'blogging_list'

    def get_queryset(self):
        return super().get_queryset().filter(publications=True)


class BloggingCreateView(CreateView):
    model = Blogging
    fields = ['header', 'content', 'img', 'publications']
    success_url = reverse_lazy('blogging:list')

    # def form_valid(self, form):
    #    form.instance.slug = slugify(form.instance.header)
    #    return super().form_valid(form)


class BloggingDetailView(DetailView):
    model = Blogging

    def get_object(self, queryset=None):
        """  Увеличивает количество просмотров """

        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save(update_fields=['views'])
        return self.object


class BloggingUpdateView(UpdateView):
    model = Blogging
    fields = ['header', 'content', 'img', 'publications']

    def get_success_url(self):
        return reverse('blogging:detail', args=[self.kwargs.get('pk')])


class BloggingDeleteView(DeleteView):
    model = Blogging
    template_name = 'blogging/blogging_delete.html'

    success_url = reverse_lazy('blogging:list')
