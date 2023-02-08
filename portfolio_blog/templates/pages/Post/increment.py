from django import template
register = template.Library()

# I'm using this in order to increment a counter inside a Django template to change color of each comment div

@register.filter
def increment(value):
    return value + 1