from drf_spectacular import openapi

class AutoSchema(openapi.AutoSchema):
    def get_tags(self):
        return ['api']
