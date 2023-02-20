from django.shortcuts import render, redirect, get_object_or_404
from url_shortener.models import LinkModel
from django.views import View


class GetCreateLinkView(View):
    def get(self, request, link_key=None):
        if link_key:
            link_object = get_object_or_404(LinkModel, link_key=link_key)
            return redirect(link_object.link)
        return render(request, 'main/index.html', {})

    def post(self, request):
        domain = request.build_absolute_uri()
        link = request.POST.get('long-link')
        link_object, _ = LinkModel.objects.get_or_create(link=link or domain)
        return render(request, 'main/index.html', {"link_object": link_object, 'domain': domain})
