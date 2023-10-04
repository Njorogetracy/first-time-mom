from django.contrib import admin
from .models import Activity, ActivityType


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