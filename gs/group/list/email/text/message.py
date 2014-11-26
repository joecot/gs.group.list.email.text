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
from zope.component import getMultiAdapter
from gs.content.email.base import (GroupEmail, TextMixin)
from .post import Post


class Message(GroupEmail):
    def __init__(self, messages, request):
        super(Message, self).__init__(messages, request)
        self.traverse_subpath = []
        self.post = None

    def publishTraverse(self, request, name):
        self.traverse_subpath.append(name)
        if self.post is None:
            # Load the post, and hook it into the aquisition tree
            self.post = Post(self.context, self.groupInfo, name)
        return self

    def __call__(self):
        tsp = self.traverse_subpath
        name = tsp[-1] if tsp > 1 else 'text'
        page = getMultiAdapter((self.post, self.request),
                               name=name)
        retval = page()
        return retval


class TextMessage(GroupEmail, TextMixin):

    def __init__(self, post, request):
        super(TextMessage, self).__init__(post, request)

    def __call__(self, *args, **kwargs):
        'Will I pass in the postId in the request or as an option. I dunno.'
        self.set_header('site-group-post.txt')
        retval = super(TextMessage, self).__call__(*args, **kwargs)
        return retval
