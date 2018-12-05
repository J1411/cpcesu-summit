from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    template_name = 'apps/core/index.html'

    context = {
        'pageId': 'core.home',
        'pagetitle': 'Home',
        'title': 'Home page',
        'bannerTemplate': 'fullscreen',
        'header': {
            'background': 'apps/core/imgs/default.jpg',
            'heading1': 'See how I got here and my future ambitions',
            'heading2': 'Looking towards the horizon',
            'buttons':[
                {
                'name': 'My History',
                'link': '/#button1'
                },
                {
                'name': 'Download Resume',
                'link': 'https://www.google.com/',
                'target': '_blank'
                }
            ]
        },
        'cssFiles': [
            'css/apps/core/testing.css'
        ]
    }

    return render(request, template_name, context)

def about(request):
    template_name = 'apps/core/about.html'

    context = {
        'pageId': 'core.about',
        'pagetitle': 'About',
        # 'title': 'Understanding More, Learning More'
    }

    return render(request, template_name, context)

def redirectHome(request):
    return HttpResponseRedirect('/')
