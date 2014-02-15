from django.shortcuts import render, redirect, render_to_response

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from post.models import Post
from post.forms import PostForm

# Create your views here.
def index(request):


    if request.method == "POST":
        # Convert
        form = PostForm(request.POST)

        # Check
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            # Create
            Post.objects.create(keyword = keyword, ip = request.META['REMOTE_ADDR'])
            return redirect('/post/')
    else:
        # Convert
        form = PostForm()
        # form = PostForm(request.GET)

        # Check
        if form.is_valid():
            pass

    page = 1
    page = request.GET.get('page')


    # Get
    entries = Post.objects.all().order_by('-created_at')

    # Show 3 per page
    paginator = Paginator(entries, 5)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)

    latest = entries.first()

    return render_to_response(
        'post/index.html',
        context_instance=RequestContext(
            request,
            {
                'form': form,
                'entries': data,
                'latest': latest,
            }
        )
    )