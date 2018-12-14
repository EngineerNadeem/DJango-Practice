from django.http import HttpResponse
from django.template import loader
from.models import Movie


def index(request):

    all_movies=Movie.objects.all()
    template = loader.get_template('movie1/index.html')
    context ={

        'all_movies ': all_movies,
    }

    return HttpResponse(template.render(context,request))


def detail(request,movie_id):
    return HttpResponse("<h1> Welcome in id :" + str(movie_id) + "</h1>")