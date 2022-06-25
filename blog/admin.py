from django.contrib import admin
from .models import Post, Comment, Category


class CommentItemInline(admin.TabularInline):
    model = Comment
    extra = 0
    raw_id_fields = ['post']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'status')
    search_fields = ('title', 'intro', 'body')
    list_filter = ['title', 'category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
