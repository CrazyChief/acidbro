# -*- coding: utf-8 -*-
import re
import os

from django import template
from django.conf import settings

from pages.models import PageBlock


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


@register.simple_tag
def retrieve_template(value):
    if value.block_type != 11:
        template_name = PageBlock.PAGE_BLOCK_TYPE[value.block_type][1]
        template_file = f'{template_name}.html'
        template_file = os.path.join(
            settings.PAGE_UPLOAD_TEMPLATE, f'{template_file}')
        return template_file


@register.simple_tag
def odd_even(value):
    return value % 2


@register.simple_tag
def divide_by_pairs(query):
    pairs = []
    first = query[::2]
    second = query[1::2]
    for i, element in enumerate(first):
        part_1 = element
        try:
            part_2 = second[i]
        except IndexError:
            part_2 = None
        pairs.append([part_1, part_2])

    return pairs
