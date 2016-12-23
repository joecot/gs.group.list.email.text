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
from zope.cachedescriptors.property import Lazy
from gs.group.list.email.base import EmailMessageViewlet


class Footer(EmailMessageViewlet):

    @Lazy
    def topicLink(self):
        'The link to the topic on the web'
        r = '{siteUrl}/r/topic/{postId}'
        retval = r.format(siteUrl=self.siteInfo.url,
                          postId=self.context.postId)
        return retval

    @Lazy
    def leaveLink(self):
        'The link to unsubscribe on the web'
        r = '{siteUrl}/groups/leave.html?groupId={groupId}'
        retval = r.format(siteUrl=self.siteInfo.url,
                          groupId=self.groupInfo.id)
        return retval

    @Lazy
    def groupName(self):
        'Group name'
        retval = self.groupInfo.name;
        return retval

    @Lazy
    def groupEmail(self):
        '''The group email address'''
        emailAddr = self.listInfo.get_property('mailto')
        retval = emailAddr
        return retval

    @Lazy
    def groupLink(self):
        'The link to the group on the web'
        retval = self.groupInfo.url;
        return retval

    @Lazy
    def policyLink(self):
        'The link to the policies on the web'
        r = '{siteUrl}/policies'
        retval = r.format(siteUrl=self.siteInfo.url)
        return retval
