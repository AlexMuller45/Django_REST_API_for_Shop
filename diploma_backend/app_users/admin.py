from django.contrib import admin

from .models import UserProfile, Cities, Payments


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'avatar')
    # search_fields = ('user', 'email', 'first_name', 'last_name')
    # ordering = 'email'


class CitiesAdmin(admin.ModelAdmin):
    pass


class PaymentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(Payments, PaymentsAdmin)


