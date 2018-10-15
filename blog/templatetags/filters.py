import re
from django import template
from django.template.defaultfilters import stringfilter
import math
from django.urls import reverse, NoReverseMatch

register = template.Library()

# Format Tags!
@register.filter
@stringfilter
def replace(value):
    value = value.replace("','", '|')
    return value.replace("'", '').title()

    
@register.filter
@stringfilter
def replaceTagsAboutme(value):
    formaTags = ""
    value = value.replace("'", '')
    value = value.split(",")
    for tag in value:
        formaTags += " #" + tag
    return formaTags.title()

@register.filter
@stringfilter
def formatFormAdminTitle(value):
    if 'blog' in value:
        value = value.replace('/administrator/', '')
    elif 'cv' in value:
        value = value.replace('/administrator/cv/', '')
    elif 'skill' in value:
        value = value.replace('/administrator/skill/', '')
    else:
        value = value.replace('/administrator/', '')

    value = value.split("/")
    extends = ' - ' + value[2] if value[2] != '' else ''
    return value[1].title() + ' ' + value[0].title() + extends 

@register.filter
@stringfilter
def formatStatic(value):
    return '/static/media/' + value

# Limit the Post Description --> Contenttext in the DB
@register.filter
@stringfilter
def limitext(value):
    return value[:405] + '...'

# Carousel Methods
@register.filter
def imagesPerSlide(value, arg):
    try:
        return math.trunc(divide(value, arg))
    except (ValueError):
        return None

@register.filter
def rangeImagesPerSlide(value, arg):
    try:
        return filter_range(0, imagesPerSlide(value, arg))
    except (ValueError):
        return None
        

# Divide by Arguments
@register.filter
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def truncate(value):
    return math.trunc(int(value))

# Remainder by Arguments
@register.filter
def remainder(value, arg):
    try:
        return int(value) % int(arg)
    except (ValueError):
        return None

# Remainder by Arguments
@register.filter
def sum(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError):
        return None

@register.filter(name='range')
def filter_range(start, end):
  return range(start, end)

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    print(pattern)
    print(path)
    if pattern == '':
        return ''
    elif re.search(pattern, path):
        return 'active'
    return ''