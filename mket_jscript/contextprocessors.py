'''
Created on Dec 12, 2013

@author: a141890
'''
import re

def ie_detector_cp(request):
    response = {}
    response['IE_VERSION'] = None
    userAgent = request.META.get('HTTP_USER_AGENT', "")
    match = re.search("MSIE (?P<version>\d{1,2}(\.\d{1,2})?)", userAgent)
    if match:
        response['IE_VERSION'] = float(match.group('version'))
    return response