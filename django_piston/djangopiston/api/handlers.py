from piston.handler import BaseHandler
from piston.utils import rc
from news.models import NewsItem

class NewsItemHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    fields = ('id', 'date', 'title', 'text')
    model = NewsItem

    def create(self, request):
        return super(NewsItemHandler, self).create(request)

    def update(self, request, news_id=None):
        data = request.data
        if news_id:
            n = self.model(id=news_id)
            n.title = data['title'] 
            n.text =data['text']
            n.save()
            return rc.ALL_OK
        else:
            resp = rc.BAD_REQUEST
            resp.write('You must specify a news item id')
            return resp

    def read(self, request, news_id=None):
        base = NewsItem.objects
        if news_id:
            return base.get(id=news_id)
        else:
            return base.all()

    def delete(self, request, news_id=None):
        if news_id:
            n = self.model(id=news_id)
            n.delete()
            return rc.DELETED
        else:
            resp = rc.BAD_REQUEST
            resp.write('You must specify a news item id')
            return resp
