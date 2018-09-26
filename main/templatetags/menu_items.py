from django import template
from django.utils.html import format_html
from django.core.urlresolvers import reverse_lazy

register = template.Library()


@register.simple_tag(takes_context=True)
def menu_item(context, label, urlname):
    cur_url = context['request'].path
    base_string = '<a class ="nav-link p-2 pr-3 ml-auto text-dark {}" href="{}">{}</a>'
    href = reverse_lazy(urlname)
    if cur_url == href:
        return format_html(base_string, 'active', href, label)
    else:
        return format_html(base_string, '', href, label)


@register.simple_tag(takes_context=True)
def menu_button(context, label, urlname):
    cur_url = context['request'].path
    base_string = '<a class="ml-auto ml-sm-3 btn btn-outline-primary {}" href="{}">{}</a>'
    href = reverse_lazy(urlname)
    if cur_url == href:
        return format_html(base_string, 'active', href, label)
    else:
        return format_html(base_string, '', href, label)