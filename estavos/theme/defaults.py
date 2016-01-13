# -*- coding: utf-8 -*-

from mezzanine.conf import register_setting

register_setting(
    name='SITE_TITLE',
    label='Site title',
    editable=False,
    default=u'Academia ESTAVOS',
)

register_setting(
    name='RICHTEXT_FILTER_LEVEL',
    label='WYSIWYG Html Filter',
    editable=False,
    default=3,
)