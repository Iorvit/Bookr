from django.contrib import admin

from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookAdmin(admin.ModelAdmin):
    model = Book 
    list_display = ('title', 'isbn_format', 'get_publisher', 'publication_date')
    search_fields = ('title', 'isbn__exact', 'publisher__name__startswith')
    date_hierarchy = 'publication_date'
    list_filter = ('publisher', 'publication_date')

    def isbn_format(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4],
                                       obj.isbn[4:6], obj.isbn[6:12],
                                       obj.isbn[12:13])

    def get_publisher(self, obj):
        return obj.publisher.name


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('creator', 'date_created', 'book', 'rating')
    list_filter = ('date_created',)
    fieldsets = (('Linkage', {'fields': ('creator', 'book', 'date_edited')}),
                ('Review content', {'fields': ('content', 'rating')})
                )


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')

    def full_name(self, obj):
        """ obj.first_names='Jerome David', obj.last_names='Salinger' => 'Salinger, JD' """
        initials = ''.join([name[0] for name in obj.first_names.split(' ')])
        return "{}, {}".format(obj.last_names, initials)


class BookContributorAdmin(admin.ModelAdmin):
    model = BookContributor
    list_display = ('contributor', 'role', 'book')


# Register your models here. 
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Review, ReviewAdmin)
