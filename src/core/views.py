from django.shortcuts import render
from .forms import CommentForm, MessageForm
from .models import Comment, Blog, Message, Testimonial

def index(request):
    blogs = Blog.objects.all()
    TMLS= Testimonial.objects.all().order_by()[:4]
    msg= False

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            
            message_count = Message.objects.filter(MSGemail=email).count()

            if message_count == 0 or message_count < 3:
                Message.objects.create(
                    MSGname=name,
                    MSGemail= email,
                    MSGsubject= subject,
                    MSGmessage= message,
                )
                msg= 'created SUCCESSFULLY'
                form = MessageForm()
            
            else:
                msg= 'SORRY, YOU have reached the ALLOWED number'
            
    else:
        form = MessageForm()

    return render(request, 'index.html', {
        'blogs': blogs,
        'TMLS':TMLS,
        'form':form,
        'msg': msg,
        })
 
def blog(request, blog_id):
    
    # Retrieve the blog post based on the post_id
    blog_post= Blog.objects.get(id=blog_id)
    all_blog= Blog.objects.all().order_by('-BLGdate')[:10]
    cmts= Comment.objects.filter(CMTblog_post=blog_post).order_by('-CMTdate')[:4]
    countCMT= Comment.objects.filter(CMTblog_post=blog_post).count()
    prgs= blog_post.paragraphs.all()
    msg=False
    

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            comment_text = form.cleaned_data['comment']
            image = form.cleaned_data['image']
            
            comment, created = Comment.objects.get_or_create(
                CMTemail=email,
                CMTblog_post=blog_post,
                defaults={
                    'CMTusername': username,
                    'CMTcomment': comment_text,
                    'CMTimage': image,
                })
            msg = 'Comment created successfully'

            if not created:
                # Comment already exists, update its information
                comment.CMTusername = username
                comment.CMTcomment = comment_text
                comment.CMTimage = image
                comment.save()
                msg= 'We UPDATE the comment'
             
              
    else:
        form = CommentForm() 
    return render(request, 'blog.html', {
        'blog_post':blog_post,
        'prgs': prgs,
        'all_blog':all_blog,
        'countCMT': countCMT,
        'cmts':cmts,
        'form':form,
        'error_msg': msg,
    })
    