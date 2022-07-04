from ast import arg
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        result = 'No page for that topic!'
        return HttpResponseNotFound(result)
        #raise Http404('Page not found!')

def add_view(request, num1, num2):
    #domain.com/my_app/num1/num2 --> result
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))

# domain.com/my_app/0 ---> domain.com/my_app/sports

def num_page_view(request, num_page):
    try:
        topics_list = list(articles.keys()) # ['sports', 'finance', 'politics']
        topic = topics_list[num_page]

        return HttpResponseRedirect(reverse('topic-page', args=[topic]))
    except:
        raise Http404('Out of range of index')
