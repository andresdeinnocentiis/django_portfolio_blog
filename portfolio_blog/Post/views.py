from django.shortcuts import render
from .models import Post, Comment, Review, Like
from UserProfile.models import AnonymousUser, UserProfile
from .forms import AddReviewForm, AddPostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import Http404
from django.db.models import Q
from .permissions import CanDelete, CanUpdate

# Para Autenticar con JWT Token:
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

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

#NOTE: BLOG POST VIEWS:
class GetPostsAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the blog posts.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [IsAuthenticated, IsAdminUser]  # Lo dejo comentado porque supongo que todos los usuarios deben poder ver los posteos
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    #authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder ver los posteos
    
    
class GetSinglePostAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single blog post.
    '''
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]  # Lo dejo comentado porque supongo que todos los usuarios deben poder ver los posteos
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication]  # Lo dejo comentado porque supongo que todos los usuarios deben poder ver los posteos

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Post.objects.get(pk=pk)
            return obj
        except Post.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}


class GetIsPostLikedByUserView(ListAPIView):
    
    serializer_class = LikeSerializer
    
    queryset = Like.objects.all()

    def get_queryset(self):
        pk = self.kwargs['pk']
        identifier = self.kwargs['identifier']

        likes = self.queryset.filter(post=pk)
        if identifier:
            likes = likes.filter(Q(user__id=identifier))
            return likes
    

class GetIsPostLikedByAnonymousUserView(ListAPIView):
    
    serializer_class = LikeSerializer
    
    queryset = Like.objects.all()

    def get_queryset(self):
        pk = self.kwargs['pk']
        identifier = self.kwargs['identifier']

        likes = self.queryset.filter(post=pk)
        if identifier:
                
            likes = likes.filter(Q(anonymous_identifier=identifier))
            return likes
        
        
    def get(self, request, pk, identifier, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_likes = self.serializer_class(queryset, many=True)
        return Response(serialized_likes.data)
        
        

      
class PostPostAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a blog post on the DataBase.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]
    
class UpdatePostAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a blog post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

class DestroyPostAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a blog post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

#NOTE: REVIEW VIEWS: =======================================================================================================================
class GetReviewsAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the posts' reviews.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class GetSingleReviewAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single review.
    '''
    serializer_class = ReviewSerializer

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Review.objects.get(pk=pk)
            return obj
        except Review.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}


class GetReviewsForPostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a all the reviews for a determined post.
    '''
    serializer_class = ReviewSerializer
    
    queryset = Review.objects.all()

    def get_queryset(self):
        postId = self.kwargs['postId']


        reviews = self.queryset.filter(post=postId)
        
        return reviews

class GetUserReviewForPostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a all the reviews for a determined post.
    '''
    serializer_class = ReviewSerializer
    
    queryset = Review.objects.all()

    def get_queryset(self):
        try:
            postId = self.kwargs['postId']
            userId = self.kwargs['userId']

            reviews_x_post = self.queryset.filter(post=postId)
            user_reviews_x_post = reviews_x_post.filter(user=userId)
            
            return user_reviews_x_post

        except Review.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}

class GetAnonymousUserReviewForPostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a all the reviews for a determined post.
    '''
    serializer_class = ReviewSerializer
    
    queryset = Review.objects.all()

    def get_queryset(self):
        try:
            postId = self.kwargs['postId']
            anonymousUserId = self.kwargs['userId']

            reviews_x_post = self.queryset.filter(post=postId)
            user_reviews_x_post = reviews_x_post.filter(anonymous_user=anonymousUserId)
            
            return user_reviews_x_post

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
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder postear reviews
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder postear reviews
    
class UpdateReviewAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a blog Review.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[CanUpdate]
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder editar sus reviews
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder editar sus reviews

class DestroyReviewAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a review.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[CanDelete]
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder eliminar sus reviews
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder eliminar sus reviews

#NOTE: COMMENT VIEWS:
class GetCommentsAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the reviews' comments.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder ver los comments
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder ver los comments
    
class GetSingleCommentAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single comment.
    '''
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

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
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder postear comments
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder postear comments
    
class UpdateCommentAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a comment.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder editar sus comments
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder editar sus comments

class DestroyCommentAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a Comment.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder eliminar sus comments
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder eliminar sus comments



#NOTE: LIKE VIEWS: ====================================================================================================================
class GetLikesAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the likes for all posts, reviews and comments.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class GetUserLikeForPostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the user like for a determined post.
    '''
    serializer_class = LikeSerializer
    
    queryset = Like.objects.all()

    def get_queryset(self):
        try:
            postId = self.kwargs['postId']
            identifier = self.kwargs['identifier']

            likes_x_post = self.queryset.filter(post=postId)
            user_like_x_post = likes_x_post.filter(user=identifier)
            
            return user_like_x_post

        except Like.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}

class GetAnonUserLikeForPostAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the anonymous user like for a determined post.
    '''
    serializer_class = LikeSerializer
    
    queryset = Like.objects.all()

    def get_queryset(self):
        try:
            postId = self.kwargs['postId']
            identifier = self.kwargs['identifier']

            likes_x_post = self.queryset.filter(post=postId)
            user_like_x_post = likes_x_post.filter(anonymous_identifier=identifier)
            
            return user_like_x_post

        except Like.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}

class GetUserLikeForReviewAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the user like for a determined review.
    '''
    serializer_class = LikeSerializer
    
    queryset = Like.objects.all()

    def get_queryset(self):
        try:
            reviewId = self.kwargs['reviewId']
            identifier = self.kwargs['identifier']

            likes_x_review = self.queryset.filter(review=reviewId)
            user_like_x_review = likes_x_review.filter(user=identifier)
            
            return user_like_x_review

        except Like.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}

class GetAnonUserLikeForReviewAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the anonymous user like for a determined review.
    '''
    serializer_class = LikeSerializer
    
    queryset = Like.objects.all()

    def get_queryset(self):
        try:
            reviewId = self.kwargs['reviewId']
            identifier = self.kwargs['identifier']

            likes_x_review = self.queryset.filter(review=reviewId)
            user_like_x_review = likes_x_review.filter(anonymous_identifier=identifier)
            
            return user_like_x_review

        except Like.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
    
class GetSingleLikeAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single like.
    '''
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

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

    
class UpdateLikeAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a like.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

class DestroyLikeAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a like.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder eliminar su like
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder eliminar su like