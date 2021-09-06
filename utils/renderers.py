from rest_framework.renderers import JSONRenderer


class EmberJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data and 'detail' in data:
            data = {'status': renderer_context.get('response').status_code,
                    'body': [],
                    'error': data.get('detail')
                    }
        elif data and 'links' in data and data['links']:
            data = {
                'status': 'OK',
                'body': data['data'],
                'error': None,
                'paging': data['links']
            }
        else:
            data = {'status': renderer_context.get('response').status_code,
                    'body': data,
                    'error': None}
        return super(EmberJSONRenderer, self).render(data, accepted_media_type, renderer_context)
