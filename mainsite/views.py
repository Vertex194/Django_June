from django.shortcuts import render, redirect
from django.template.loader import get_template 
from django.http import HttpResponse
from datetime import datetime
from.models import Post
# Create your views here.
def homepage(request):
    template = get_template('blog_index.html')
    posts = Post.objects.all().order_by('slug')
    #post_lists = list()
    now = datetime.now()
    '''
    for count, post in enumerate(posts):
        post_lists.append("No.{}".format(str(count))+str(post)+"<br>")
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    '''
    #return HttpResponse(post_lists)
    html = template.render(locals())  
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post!= None:
            html = template.render(locals())  
            return HttpResponse(html)
    except:
        return redirect('/')