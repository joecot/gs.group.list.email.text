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
from __future__ import absolute_import, unicode_literals, print_function
from email.mime.text import MIMEText
from zope.component import getMultiAdapter
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


class TextMessagePart(object):
    '''The text message a part, that can be used to make an email'''
    #: The weight, used for sorting the different message-types
    weight = 10
    #: The show property is used to determine if the message part should be shown
    show = True

    def __init__(self, post, request):
        self.post = self.context = post
        self.request = request

    def as_email(self):
        '''The message as an email-component

:returns: An instance of the core email-message class containing the plain
          text form of the post. The MIME-type of the message is
          :mimetype:`text/plain`, and the encoding is UTF-8.
:rtype: :class:`email.mime.text.MIMEText`'''
        # Normally the textMessage is a TextMessage, above.
        textMessage = getMultiAdapter((self.context, self.request), name="text")
        text = textMessage()
        retval = MIMEText(text, 'plain', 'utf-8')

        return retval
