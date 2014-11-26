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
from __future__ import (absolute_import, division, unicode_literals)
from zope.cachedescriptors.property import Lazy
from Products.XWFMailingListManager import MessageQuery


class Post(object):

    def __init__(self, groupInfo, postId):
        if not postId:
            raise ValueError('Post identifier required')
        self.groupInfo = groupInfo
        self.postId = postId

    @Lazy
    def id(self):
        return self.postId

    @Lazy
    def post(self):
        query = MessageQuery(self.groupInfo.groupObj)
        retval = query.post(self.postId)
        if ((retval['group_id'] != self.groupInfo.id)
           or (retval['site_id'] != self.groupInfo.siteInfo.id)):
                m = 'Post "{0}" not in the group {1} on {2}'
                msg = m.format(self.postId, self.grouInfo.id,
                               self.groupInfo.siteInfo.id)
                raise ValueError(msg)
        return retval

    @Lazy
    def body(self):
        retval = self.post['body']
        return retval

    @Lazy
    def files(self):
        retval = [File.from_query_dict(self.groupInfo, d)
                  for d in self.post['files_metadata']]
        return retval


class File(object):

    def __init__(self, groupInfo, fileId, name, rawSize, mimeType):
        self.name = name
        self.size = '{0:.1f}kb'.format(rawSize / 1024.0)
        self.mimeType = mimeType
        u = '{0}/r/file/{1}/'
        self.url = u.format(groupInfo.siteInfo.url, fileId)

    @classmethod
    def from_query_dict(cls, groupInfo, d):
        retval = cls(groupInfo, d['file_id'], d['file_name'],
                     d['file_size'], d['mime_type'])
        return retval
