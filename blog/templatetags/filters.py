import re
from django import template
from django.template.defaultfilters import stringfilter
from django.urls import reverse, NoReverseMatch

register = template.Library()

# Format Tags!
@register.filter
@stringfilter
def replace(value):
    value = value.replace("','", '|')
    return value.replace("'", '').title()

# Limit the Post Description --> Contenttext in the DB
@register.filter
@stringfilter
def limitext(value):
    return value[:405] + '...'


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''