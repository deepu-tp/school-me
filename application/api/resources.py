from tastypie.resources import ModelResource
from application.models import Payment, Application
from tastypie.authentication import ApiKeyAuthentication

'''
class CBSEApplicationResource(ModelResource):
	class Meta:
		queryset = CBSEApplication.objects.all()
		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()

class StateApplicationResource(ModelResource):
	class Meta:
		queryset = StateApplication.objects.all()
		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()

class MontessoriApplicationResource(ModelResource):
	class Meta:
		queryset = MontessoriApplication.objects.all()
		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()

'''

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