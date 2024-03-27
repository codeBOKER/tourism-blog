from django.contrib import admin
from .models import Blog, Paragraph, Comment, Writer, Message, Testimonial

admin.site.register(Comment)
admin.site.register(Writer)
admin.site.register(Message)
admin.site.register(Testimonial)

class ParagraphInline(admin.StackedInline):
    model = Paragraph
    extra = 1



class BlogAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]



admin.site.register(Blog, BlogAdmin)

