from django.contrib.syndication.views import Feed
from eblog.models import Entry

class LatestPosts(Feed):
    title = "evilroot's blog"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Entry.objects.published()[:5]
