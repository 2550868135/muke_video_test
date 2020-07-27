''' @File :base_render.py @Author:张宇 @Date :2020/7/27 17:39 @Desc : '''
from mako.lookup import TemplateLookup
from django.template import RequestContext
from django.conf import settings  # 用于获取templates地址
from django.template.context import Context
from django.http import HttpResponse


def render_to_response(request, template, data=None):
    # 创建请求上下文实例
    context_instance = RequestContext(request)
    # 获取template地址
    path = settings.TEMPLATES[0]['DIRS'][0]

    # 注册mako的模板
    lookup = TemplateLookup(
        directories=path,
        input_encoding='utf-8',
        output_encoding='utf-8'
    )
    
    #得到要渲染的template的地址
    mako_template = lookup.get_template(template)
    
    if not data:
        data = {}
        
    if context_instance:
        context_instance.update(data)
    else:
        context_instance = Context(data)
        
    result = {}
    
    for d in context_instance:
        result.update(d)
    
    result['csrf_token'] = '<input type="hidden" name="csrfmiddlewaretoken" value={} />'.format(request.META.get('CSRF_COOKIE'))

    return HttpResponse(mako_template.render(**result))

