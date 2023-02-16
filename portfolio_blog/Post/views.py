from django.shortcuts import render
from .models import Post, Comment, Review, Like
from UserProfile.models import AnonymousUser, UserProfile
from .forms import AddReviewForm, AddPostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import Http404

# Django REST Framework imports:
from .serializers import PostSerializer, ReviewSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

# Create your views here.

# BORRAR ESTAS VIEWS PORQUE SE VAN A MANEJAR DESDE EL FRONT
def get_all_posts(request):
    
    posts = Post.objects.all()
    
    context = {
        'posts': posts,   
    }
    
    return render(request, 'pages/Post/all_posts.html', context)


def add_review_form(request, post_id):
    
    post = Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        review_form = AddReviewForm(request.POST, user = request.user, anonymous_identifier=request.COOKIES.get('cookie_name'))
        
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
                cookie_value = request.COOKIES.get('value')
                anonymous_user = AnonymousUser.objects.create(username=info['user'], anonymous_identifier=cookie_value)
                review.anonymous_user = anonymous_user
            
            review.save()
            
            return redirect(f'pages/Post/post_detail.html')
    
    else:
        review_form = AddReviewForm(user = request.user, anonymous_identifier = request.COOKIES.get('value'))
        
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


#NOTE: BLOG POST VIEWS:
class GetPostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the blog posts.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSinglePostAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single blog post.
    '''
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Post.objects.get(pk=pk)
            return obj
        except Post.DoesNotExist:
            raise Http404
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
    This API view deletes a blog post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#NOTE: REVIEW VIEWS:
class GetReviewAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the posts' reviews.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSingleReviewAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single review.
    '''
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Review.objects.get(pk=pk)
            return obj
        except Review.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostReviewAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a review for a post on the DataBase.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdateReviewAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a blog Review.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyReviewAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a review.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#NOTE: COMMENT VIEWS:
class GetCommentAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the reviews' comments.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSingleCommentAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single comment.
    '''
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Comment.objects.get(pk=pk)
            return obj
        except Comment.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostCommentAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a comment for a review or for another comment on the DataBase.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdateCommentAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a comment.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyCommentAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a Comment.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#NOTE: LIKE VIEWS:
class GetLikeAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the likes for all posts, reviews and comments.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSingleLikeAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single like.
    '''
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Like.objects.get(pk=pk)
            return obj
        except Like.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostLikeAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a like for a related post, review or comment on the DataBase.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdateLikeAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a like.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyLikeAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a like.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]