# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from gs.content.email.base import (GroupEmail, TextMixin)
from .post import Post


class TextMessage(GroupEmail, TextMixin):

    def __init__(self, group, request):
        super(TextMessage, self).__init__(group, request)
        self.postId = request.get('postId', None)

    def __call__(self, *args, **kwargs):
        'Will I pass in the postId in the request or as an option. I dunno.'
        self.set_header('site-group-post.txt')
        self.postId = kwargs.get('postId', self.postId)
        self.post = Post(self.groupInfo, self.postId)
        retval = super(TextMessage, self).__call__(*args, **kwargs)
        return retval
