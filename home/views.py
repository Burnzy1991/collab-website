from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import Comment
from django.views import generic
from .models import Post
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
# Create your views here.



class HomeView(TemplateView):
    template_name = "home.html"


def post_detail(request):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
