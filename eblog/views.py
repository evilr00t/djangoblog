from django.views import generic
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "base.html"
    paginate_by = 3

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

class AboutMe(generic.TemplateView):
    template_name = "aboutme.html"
