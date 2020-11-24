# -*- coding: utf-8 -*-
import re

from django import template


register = template.Library()


@register.simple_tag
def check_img(value):
    if re.search(r".svg$", value):
        return 'svg+xml'
    elif re.search(r".(jpg|jpeg)$", value):
        return 'jpeg'
    elif re.search(r".png$", value):
        return 'png'
    elif re.search(r".gif$", value):
        return 'gif'
