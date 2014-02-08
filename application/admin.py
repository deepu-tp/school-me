from django.contrib import admin

# Register your models here.

from models import Application, Payment

class PaymentAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('name', 'mode', 'amount')
			}),
		('Additional Information', {
			'fields': ('info', )
			})
	)
	list_display = ( 'name', 'mode', 'amount', 'info', )

class ApplicationAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('name', 'gender', 'dob', 'placeofbirth', 'religion')
			}),
		('Parent Information', {
			'fields': ('parentonename', 'parentonephone', 'parentoneemail', 'parenttwoname', 'parenttwophone', 'parenttwoemail'),
			}),
		('Payment Information', {
			'fields': ('payment', )
			})
	)
	list_display = ( 'id', 'name', 'gender', 'parentonename', 'parentonephone', 'parentoneemail', )

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Payment, PaymentAdmin)