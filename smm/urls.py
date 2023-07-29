from django.urls import path
from smm.apps import SmmConfig
from smm.views import ServiceClientListView, ServiceClientCreateView, ServiceClientDetailView, ServiceClientUpdateView, \
    ServiceClientDeleteView, NewsletterListView, NewsletterCreateView, NewsletterDetailView, NewsletterUpdateView, \
    NewsletterDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailinglogsListView, MailinglogsCreateView, MailinglogsDetailView, MailinglogsUpdateView, MailinglogsDeleteView

app_name = SmmConfig.name

urlpatterns = [
    path('', ServiceClientListView.as_view(), name='list'),
    path('smm_create/', ServiceClientCreateView.as_view(), name='create'),
    path('smm_detail/<int:pk>/', ServiceClientDetailView.as_view(), name='detail'),
    path('smm_update/<int:pk>/', ServiceClientUpdateView.as_view(), name='update'),
    path('smm_delete/<int:pk>/', ServiceClientDeleteView.as_view(), name='delete'),

    path('news_letter_list/', NewsletterListView.as_view(), name='letter_list'),
    path('news_letter_create/', NewsletterCreateView.as_view(), name='letter_create'),
    path('news_letter_detail/<int:pk>/', NewsletterDetailView.as_view(), name='letter_detail'),
    path('news_letter_update/<int:pk>/', NewsletterUpdateView.as_view(), name='letter_update'),
    path('news_letter_delete/<int:pk>/', NewsletterDeleteView.as_view(), name='letter_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('mailinglogs_list', MailinglogsListView.as_view(), name='mailinglogs_list'),
    path('mailinglogs_create/', MailinglogsCreateView.as_view(), name='mailinglogs_create'),
    path('mailinglogs_detail/<int:pk>/', MailinglogsDetailView.as_view(), name='mailinglogs_detail'),
    path('mailinglogs_update/<int:pk>/', MailinglogsUpdateView.as_view(), name='mailinglogs_update'),
    path('mailinglogs_delete/<int:pk>/', MailinglogsDeleteView.as_view(), name='mailinglogs_delete'),
]
