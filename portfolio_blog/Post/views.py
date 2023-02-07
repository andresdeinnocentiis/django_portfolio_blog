from django.shortcuts import render
from .models import Post, Comment, Review
from UserProfile.models import AnonymousUser
from .forms import AddReviewForm, AddPostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

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
                review.user = request.user.username
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