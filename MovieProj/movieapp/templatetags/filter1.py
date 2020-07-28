from django import template
register=template.Library()

@register.filter(name='k')
def truncate2(value):
    result=value[0:3]
    return result
#register.filter('truncate2',truncate2)
