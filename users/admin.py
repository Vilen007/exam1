from django.contrib import admin

# Register your models here.
from .models import User_Table, User_Role, Users_Rights, User_assign_role

# Register your models here.
admin.site.register(User_Table),
admin.site.register(User_Role),
admin.site.register(Users_Rights),
admin.site.register(User_assign_role)
