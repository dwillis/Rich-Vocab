from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from vocab.utils import yule

@csrf_protect
def home(request):
    if request.method == 'POST':
        text = request.POST['text']
        score = yule(text)
    else:
        score = None
        text = None
    return render_to_response('home.html', {'score': score, 'text': text }, context_instance=RequestContext(request))