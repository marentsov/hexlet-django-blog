from django.http import HttpResponse
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('articles')
#def index(request):
    #name = 'articles'
    #return render(
        #request,
        #'articles/index.html',
        #context={'name': name},
    #)


# Create your views here.
