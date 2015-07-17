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
from gs.group.base import GroupViewlet
from Products.GSGroup.interfaces import (IGSMailingListInfo)


# FIXME: I am unsure why I cannot get the acquisition to work, so the
# GroupViewlet.groupInfo and GroupInfo.siteInfo properties fail to get
# the site an group. This is a hack to get around that issue.

class EmailMessageViewlet(GroupViewlet):

    @Lazy
    def listInfo(self):
        retval = IGSMailingListInfo(self.groupInfo.groupObj)
        return retval
