from django.contrib import admin
#from . import models
from .models import *
from django.conf import settings
from paypalrestsdk import configure, Payout

configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})



class TransactionAdmin(admin.ModelAdmin):
    # Step 1: To display more column in Admin Dashboard -> go to Step 2
    list_display = ['stripe_payment_intent_id', 'courier_paypal_email', 'customer', 'courier', 'job', 'amount', 'status', 'created_at']
    list_filter = ['status', ] # If there is only one field, you have to add ',' at the end


    # Only you have define belows method, so that you can display extra fields which are not orginally inside Transaction Model
    def customer(self, obj):
        return obj.job.customer # The object refers to Transaction, and the 'job' is linked to the Transaction Model 
                                # job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def courier(self, obj):
        return obj.job.courier

    def courier_paypal_email(self, obj):
        return obj.job.courier.paypal_email if obj.job.courier else None



# Register your models here.
admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Transaction, TransactionAdmin)