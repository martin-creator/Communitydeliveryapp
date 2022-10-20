from django.contrib import admin
#from . import models
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Transaction)