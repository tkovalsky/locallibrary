from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    
    """
    You can add "sections" to group related model information within the detail form, using the fieldsets attribute.
    Each section has its own title (or None, if you don't want a title)
    """
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }) 
     )



admin.site.register(Language)



"""
the @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax):
"""
