from django.shortcuts import render
from .models import Post, Comment, Review
from UserProfile.models import AnonymousUser, UserProfile
from .forms import AddReviewForm, AddPostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Django REST Framework imports:
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

# Create your views here.
"""
BORRAR ESTAS VIEWS PORQUE SE VAN A MANEJAR DESDE EL FRONT
def get_all_posts(request):
    
    posts = Post.objects.all()
    
    context = {
        'posts': posts,   
    }
    
    return render(request, 'pages/Post/all_posts.html', context)


def add_review_form(request, post_id):
    
    post = Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        review_form = AddReviewForm(request.POST, user = request.user)
        
        if review_form.is_valid():
            
            info = review_form.cleaned_data
            
            review = Review(
                post = post,
                rating = info['rating'],
                content = info['content']
            )
            
            if request.user.is_authenticated:
                review.user = request.user

            else:
                anonymous_user = AnonymousUser.objects.create(name=info['user'])
                review.anonymous_user = anonymous_user
            
            review.save()
            
            return redirect(f'pages/Post/post_detail.html')
    
    else:
        
        review_form = AddReviewForm(user = request.user)
        
    return render(request, 'pages/Post/post_detail.html', {'review_form': review_form})


def get_post(request, pk):
    
    post = Post.objects.get(pk = pk)
    reviews = Review.objects.all()
    comments = Comment.objects.all()
    review_form = AddReviewForm(user= request.user)
    
    context = {
        'post': post,
        'reviews': reviews,
        'comments': comments,
        
        # ESTO SE LO TENGO QUE PASAR: 1. Para que me muestre el form dentro de esta otra view, 2. Para que cumpla con la función de la otra view, dentro de esta view.
        'review_form': review_form,
        'add_review_form': add_review_form(request,post.pk)
    }
    
    return render(request, 'pages/Post/post_detail.html', context)


def add_post(request):
    if request.method == "POST":
        post_form = AddPostForm(request.POST)
        if post_form.is_valid():
            
            info = post_form.cleaned_data
                
            post = Post(
                title =  info['title'],
                caption = info['caption'],
                image = info['image'],
                description = info['description'],
                tech_used = info['tech_used'],
                github_link = info['github_link'],
                website_link = info['website_link']
            )
            
            post.save()
            
            return redirect('/posts')
    
    else:
        
        post_form = AddPostForm()
        
    return render(request, 'pages/Post/create_post_form.html', {'post_form': post_form})
"""

# BLOG POST VIEWS:
class GetPostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the blog posts.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSinglePostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single blog post.
    '''
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        '''
        Sobrescribimos la función `get_queryset` para poder filtrar el request 
        por medio de la url. En este caso traemos de la url por medio de `self.kwargs` 
        el parámetro `Post_id` y con él realizamos una query para traer 
        el Post del ID solicitado.  
        '''
        try:
            id = self.kwargs['id']
            queryset = Post.objects.filter(id=id)
            return queryset
        
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostPostAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a blog post on the DataBase.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdatePostAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a blog post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyPostAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view updates a blog post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]