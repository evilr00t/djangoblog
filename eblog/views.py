from django.views import generic
#from django.db.models import F
from . import models
from hitcount.views import HitCountDetailView


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 3

class BlogDetail(HitCountDetailView, generic.DetailView):
    count_hit = True
    model = models.Entry
    template_name = "post.html"

class AboutMe(generic.TemplateView):
    template_name = "aboutme.html"
