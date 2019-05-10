from django.http import HttpResponse

#导包
import logging
#创建日志实例,
logger = logging.getLogger('django')

def log(request):
    # 记录日志
    logger.info('lalalallal')

    return HttpResponse('log')