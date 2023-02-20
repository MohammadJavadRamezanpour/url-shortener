from django.urls import path
from url_shortener.views import GetCreateLinkView

app_name = 'url_shortener'

urlpatterns = [
    path('', GetCreateLinkView.as_view(), name="getCreateLinkView"),
    path('<str:link_key>', GetCreateLinkView.as_view(), name="getCreateLinkView"),
]
