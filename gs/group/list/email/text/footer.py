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
from zope.cachedescriptors.property import Lazy
from gs.group.base import GroupViewlet
from Products.GSGroup.interfaces import (IGSMailingListInfo)


class Footer(GroupViewlet):
    @Lazy
    def groupInfo(self):
        retval = self.context.groupInfo
        return retval

    @Lazy
    def siteInfo(self):
        retval = self.groupInfo.siteInfo
        return retval

    @Lazy
    def listInfo(self):
        retval = IGSMailingListInfo(self.groupInfo.groupObj)
        return retval

    @Lazy
    def topicLink(self):
        'The link to the topic on the web'
        r = '{siteUrl}/r/topic/{postId}'
        retval = r.format(siteUrl=self.context.groupInfo.siteInfo.url,
                          postId=self.context.postId)
        return retval

    @Lazy
    def leaveLink(self):
        '''The leave link. Some cut-n-paste software engineering from
``gs.group.list.sender.headers.simpleadd.ListUnsubscribe``'''
        emailAddr = self.listInfo.get_property('mailto')
        retval = 'mailto:{0}?Subject=Unsubscribe'.format(emailAddr)
        return retval
