from tastypie.resources import ModelResource
from application.models import Payment, Application
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie import fields

class PaymentResource(ModelResource):
	class Meta:
		queryset = Payment.objects.all()
		allowed_methods = ['post']
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()
		always_return_data = True

class ApplicationStatusResource(ModelResource):
	class Meta:
		queryset = Application.objects.all()
		allowed_methods = ['get']
		fields = ('status', )
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()
		always_return_data = True

class ApplicationResource(ModelResource):
	payment = fields.ForeignKey(PaymentResource, 'payment')
	class Meta:
		queryset = Application.objects.all()
		allowed_methods = ['post']
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()
		always_return_data = True
