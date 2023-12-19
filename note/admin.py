# Register your models here.
from django.contrib import admin
from .models import Category, NotePost, Comment, Announcement  #reaction


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class NotePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(NotePost, NotePostAdmin)
admin.site.register(Announcement)


#admin.site.register(Reaction)