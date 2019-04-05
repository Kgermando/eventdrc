from django.urls import path

from eventApp.views import index, contact, about, details, presentation, prix


urlpatterns = [
    path('', index, name='index'),
    path('details/<id>/', details, name='details'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('presentation', presentation, name='presentation'),
    path('pricing', prix, name='prix')
]
