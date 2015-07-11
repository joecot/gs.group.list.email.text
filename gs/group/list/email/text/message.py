# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014, 2015 OnlineGroups.net and Contributors.
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


class TextMessage(GroupEmail, TextMixin):
    '''The actual *page* for the text version of a post.

:param post: The post to render
:type post: gs.group.list.email.base.interfaces.IPost
:param request: The Zope request

Mostly this class exists just to set the correct headers. The heavy-lifting
is done by the viewlets.'''
    def __init__(self, post, request):
        super(TextMessage, self).__init__(post, request)

    def __call__(self, *args, **kwargs):
        self.set_header('post-{0}.txt'.format(self.context.postId))
        retval = super(TextMessage, self).__call__(*args, **kwargs)
        return retval
