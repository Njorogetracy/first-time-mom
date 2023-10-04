from django.contrib import admin
from .models import Activity, Review


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'max_participants',)
    list_filter = ('date', 'activity_type')
    search_fields = ('activity_name', 'description')
    raw_id_fields = ('activity_type',)


# @admin.register(ActivityType)
# class ActivityType(admin.ModelAdmin):
#     list_display = ('type',)
#     list_filter = ('type',)
#     search_fields = ('type',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('activity', 'user', 'rating', 'approved', 'created_on')
    list_filter = ('approved',)
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'{queryset.count()} review approved.')