from django.shortcuts import render
from .models import Post, Comment, Review, Like
from UserProfile.models import AnonymousUser, UserProfile
from .forms import AddReviewForm, AddPostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import Http404
from django.db.models import Q

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
        print("IDENTIFIER: ", identifier)
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
        print("IDENTIFIER: ", identifier)
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

#NOTE: REVIEW VIEWS:
class GetReviewsAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the posts' reviews.
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]  # Lo dejo comentado porque supongo que todos los usuarios deben poder ver las reviews
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder ver las reviews
    
class GetSingleReviewAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single review.
    '''
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

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

#NOTE: LIKE VIEWS:
class GetLikesAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the likes for all posts, reviews and comments.
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    
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
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder dejar un like
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder dejar un like
    
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