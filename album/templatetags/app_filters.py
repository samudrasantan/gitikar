from django import template
register = template.Library()


@register.filter(name='alf')

def alf(value):
    newlist=[x[0] for x in value]
    return newlist

@register.filter(name='sor')
def sor(value):
    newsor = sorted(value.keys())
    return newsor