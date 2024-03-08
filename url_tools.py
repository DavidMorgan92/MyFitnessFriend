from django.urls import reverse
from django.utils.http import urlencode


# https://stackoverflow.com/questions/9585491/how-do-i-pass-get-parameters-using-django-urlresolvers-reverse
def reverse_with_params(*args, **kwargs):
    """Reverse resolve a URL and add URL parameters"""

    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    
    if get:
        url += '?' + urlencode(get)

    return url
