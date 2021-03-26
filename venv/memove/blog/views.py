from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
                                    PageNotAnInteger
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    queryset= Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    

class PostCreateView( LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'body', 'address', 'city', 'postcode','number_of_beds',
    'number_of_baths','price','property_type','property_pic' ]
    template_name = 'blog/post/post_creation.html'
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



'''def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                'blog/post/list.html',
            {'page': page, 'posts': posts})'''

def post_detail(request, pk ,slug):
    post = get_object_or_404(Post, id=pk , status = 'published')
    return render(request, 'blog/post/detail.html', {'post':post})

#publish__year = year,
#publish__month = month,
#publish__day = day
