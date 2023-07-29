from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from smm.models import ServiceClient, Newsletter, Message, Mailinglogs


class ServiceClientListView(ListView):
    model = ServiceClient


class ServiceClientCreateView(CreateView):
    model = ServiceClient
    fields = ['email', 'fullname', 'comment']
    success_url = reverse_lazy('smm:list')


class ServiceClientDetailView(DetailView):
    model = ServiceClient


class ServiceClientUpdateView(UpdateView):
    model = ServiceClient
    fields = ['email', 'fullname', 'comment']

    def get_success_url(self):
        return reverse('smm:detail', args=[self.kwargs.get('pk')])


class ServiceClientDeleteView(DeleteView):
    model = ServiceClient
    success_url = reverse_lazy('smm:list')


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ['mailing_time', 'mailing_status']
    success_url = reverse_lazy('smm:letter_list')


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ['mailing_time', 'mailing_status']

    def get_success_url(self):
        return reverse('smm:letter_detail', args=[self.kwargs.get('pk')])


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('smm:letter_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ['letter_subject', 'letter_body']
    success_url = reverse_lazy('smm:message_list')


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['letter_subject', 'letter_body']

    def get_success_url(self):
        return reverse('smm:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('smm:message_list')


class MailinglogsListView(ListView):
    model = Mailinglogs


class MailinglogsCreateView(CreateView):
    model = Mailinglogs
    fields = ['last_attempt', 'attempt_status', 'mail_server']
    success_url = reverse_lazy('smm:mailinglogs_list')


class MailinglogsDetailView(DetailView):
    model = Mailinglogs


class MailinglogsUpdateView(UpdateView):
    model = Mailinglogs
    fields = ['last_attempt', 'attempt_status', 'mail_server']

    def get_success_url(self):
        return reverse('smm:mailinglogs_detail', args=[self.kwargs.get('pk')])


class MailinglogsDeleteView(DeleteView):
    model = Mailinglogs
    success_url = reverse_lazy('smm:mailinglogs_list')
