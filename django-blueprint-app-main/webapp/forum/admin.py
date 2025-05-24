# forum/admin.py
from django.contrib import admin
from .models import KoloMembership, ForumPost

@admin.register(KoloMembership)
class KoloMembershipAdmin(admin.ModelAdmin):
    list_display    = ('user', 'kolo')
    search_fields   = ('user__username', 'kolo')
    list_filter     = ('kolo',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display    = ('author', 'kolo', 'created_at', 'short_content')
    search_fields   = ('author__username', 'content')
    list_filter     = ('kolo', 'created_at')
    date_hierarchy  = 'created_at'

    def short_content(self, obj):
        return obj.content[:50] + ('…' if len(obj.content) > 50 else '')
    short_content.short_description = 'Content-preview'
