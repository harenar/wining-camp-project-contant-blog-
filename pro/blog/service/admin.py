from django.contrib import admin
from service.models import Service
from service.models import Reg

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('username','Ctitle','description')

class RegiUser(admin.ModelAdmin):
    list_user = ('name','reg_user_name','password')

admin.site.register(Service,ServiceAdmin)

#registation model
admin.site.register(Reg,RegiUser)

# Register your models here.
