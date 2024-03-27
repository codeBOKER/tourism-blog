from django.db import models

class Blog(models.Model):
    BLGwriter = models.ForeignKey("Writer", verbose_name=("writer"), on_delete=models.CASCADE)
    BLGtitle = models.CharField(max_length=255)
    BLGheader = models.CharField(max_length=80)
    BLGdate = models.DateTimeField(("Date"), auto_now=False, auto_now_add=False)
    BLGimage = models.ImageField(("blog image"), upload_to="media/images/%y/%m/%d")
    BLGcontent = models.TextField()
    # count comments in a blog
    def BLGcountCMT(self):
        return self.comment_set.count()

    def __str__(self):
        return "{}--{}".format(self.BLGtitle, str(self.BLGwriter))

class Writer(models.Model):
    WRTRname= models.CharField(("name"), max_length=50)
    WRTRimage= models.ImageField(("photo"), upload_to="media/writer/%y/%m/%d", null=True, blank=True)
    WRTRbio= models.TextField(("bio"))

    def __str__(self):
        return str(self.WRTRname)
    

class Paragraph(models.Model):  
    PARblog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='paragraphs')
    PARtitle = models.CharField(("title of paragraph"), max_length=255, null=True, blank=True)
    PARimage = models.ImageField(("blog image"), upload_to="media/images/%y/%m/%d", blank=True, null=True)
    PARcontent = models.TextField()

    def __str__(self):
        return "Paragraph {} of {}".format(self.id, self.PARblog)

class Comment(models.Model):
    CMTusername = models.CharField(max_length=255)
    CMTimage = models.ImageField(upload_to="media/users_photo/%y/%m/%d", null=True, blank=True)
    CMTemail = models.EmailField()
    CMTcomment = models.TextField()
    CMTdate = models.DateTimeField(("Date"), auto_now=False, auto_now_add=True, auto_created=True)
    CMTblog_post = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.CMTusername)

class Message(models.Model):
    MSGname= models.CharField(("name"), max_length=50)
    MSGemail= models.EmailField(("email"), max_length=254)
    MSGsubject= models.CharField(("subject"), max_length=50)
    MSGmessage= models.TextField(("message"))
    
    def __str__(self):
        return self.MSGname
    
class Testimonial(models.Model):
    TMLname= models.CharField(("name"), max_length=50)
    TMLexperiance= models.TextField(("experiance"))
    TMLimage= models.ImageField(("photo"), upload_to="media/users_photo/experiance/%y/%m/%d",)
    TMLdate= models.DateTimeField(("Date"), auto_now=False, auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.TMLname

    


    

    





    


