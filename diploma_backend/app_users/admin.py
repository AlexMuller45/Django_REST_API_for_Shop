from django.contrib import admin

from .models import UserProfile, Cities, Payments


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'avatar')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = 'email'


class CitiesAdmin(admin.ModelAdmin):
    pass


class PeymentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(Payments, PeymentsAdmin)



