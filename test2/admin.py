from django.contrib import admin
from .models import t2Type, T2Question, result_t2
# Register your models here.
admin.site.register(T2Question)
admin.site.register(t2Type)
admin.site.register(result_t2)
