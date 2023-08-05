from django.contrib import admin

from .models import JobRole, UserRole, CompanyRole

# Register your models here.

admin.site.register(JobRole)
admin.site.register(UserRole)
admin.site.register(CompanyRole)
