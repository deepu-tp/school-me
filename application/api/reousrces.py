from tastypie.resources import ModelResource
from application.models import Application, Payment
from tastypie.authentication import ApiKeyAuthentication

class ApplicationResource(ModelResource):
	class Meta:
		queryset = Application.objects.all()
		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()

class PaymentResource(ModelResource):
	class Meta:
		queryset = Payment.objects.all()
		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()