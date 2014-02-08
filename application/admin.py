from django.contrib import admin

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
			'fields': ('parent_one_name', 'parent_one_phone', 'parent_one_email', 'parent_two_name', 'parent_two_phone', 'parent_two_email'),
			}),
		('Payment Information', {
			'fields': ('payment', )
			})
	)
	list_display = ( 'id', 'name', 'gender', 'parent_one_name', 'parent_one_phone', 'parent_one_email', )

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Payment, PaymentAdmin)