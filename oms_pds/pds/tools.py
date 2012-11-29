#from tastytools.api import Api
from tastypie.api import Api
from oms_pds.pds.api import FunfResource, FunfConfigResource, RoleResource, PurposeResource, AnswerResource, AnswerListResource, AuditEntryResource, AuditEntryCountResource

v1_api = Api(api_name='personal_data')
v1_api.register(FunfResource())
v1_api.register(FunfConfigResource())
v1_api.register(RoleResource())
v1_api.register(PurposeResource())
v1_api.register(AnswerResource())
v1_api.register(AnswerListResource())
v1_api.register(AuditEntryResource())
v1_api.register(AuditEntryCountResource())

