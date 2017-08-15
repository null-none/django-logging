#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging

from django.http import FileResponse

request_params_logger = logging.getLogger('request_logging.request_params')
request_logger = logging.getLogger('request_logging.request')
error_logger = logging.getLogger('request_logging.request')

class RequestLoggingMiddleware(object):

    def get_client_ip(self, request):
        real_ip = request.META.get('HTTP_X_REAL_IP')
        if real_ip:
            return real_ip
        return request.META.get('REMOTE_ADDR')

    def process_request(self, request):
        request._request_start_time = time.time()

        headers = {k: request.META[k] for k in request.META.keys() if k.startswith('HTTP_')}
        headers['CONTENT_TYPE'] = request.META.get('CONTENT_TYPE', '-')
        headers['CONTENT_LENGTH'] = request.META.get('CONTENT_LENGTH', '-')
        try:
            body = repr(request.body)
        except:
            body = '-ERR-'

        if hasattr(request, 'user'):
            user_str = '{}({})'.format(request.user.username, request.user.id)
        else:
            user_str = 'None'

        msg = '{method} {path} u:{user_str} GET={get} POST={post} META={meta} BODY={body} FILES={files}'.format(
            method=repr(request.method),
            path=repr(request.path),
            get=repr(dict(request.GET)),
            post=repr(dict(request.POST)),
            files=repr(dict(request.FILES)),
            body=body,
            meta=repr(headers),
            user_str=user_str
        )
        request_params_logger.info(msg)

    def process_response(self, request, response):
        if hasattr(request, '_request_start_time'):
            request._request_end_time = time.time()
            request._request_process_time = 1000. * (request._request_end_time - request._request_start_time)
            time_str = '{:.0f}ms'.format(request._request_process_time)
        else:
            time_str = '-'

        if hasattr(request, 'user'):
            user_str = '{}({})'.format(request.user.username, request.user.id)
        else:
            user_str = 'None'

        if isinstance(response, FileResponse):
            content_length = int(response['content-length'])
            if content_length == 0:
                content_length = 'streaming'
        else:
            content_length = len(response.content)

        msg = 'ip:{ip} u:{user} t:{time} s:{status} len:{length} ct:"{content_type}" {method} {path} '.format(
            method=repr(request.method),
            path=repr(request.path),
            user=user_str,
            ip=self.get_client_ip(request),
            time=time_str,
            status=response.status_code,
            length=content_length,
            content_type=response.get('Content-Type'),
        )
        request_logger.info(msg)
        return response
