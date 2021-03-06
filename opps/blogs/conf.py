#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings

from appconf import AppConf


class OppsBlogsConf(AppConf):
    BLOG_TYPES = (
        ('blog', 'Blog'),
    )

    CHANNEL = getattr(settings, 'OPPS_BLOGS_CHANNEL', 'blog')
    PROFILE = getattr(settings, 'OPPS_BLOGS_PROFILE', False)
    TYPES = getattr(settings, 'OPPS_BLOGS_TYPES', BLOG_TYPES)

    class Meta:
        prefix = 'opps_blogs'
