from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'deposit/deposit_list.html'

