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
from .queries import MessageQuery


class Post(object):
    '''A post made to a group

:param messages: The messages folder of a group.
:type messages: Products.XWFMailingListManager.interfaces.IGSMessagesFolder
:param groupInfo: The information about the current group.
:type groupInfo: Products.GSGroup.interfaces.IGSGroupInfo
:param str postId: The identifier for the post.'''
    def __init__(self, messages, groupInfo, postId):
        if not postId:
            raise ValueError('Post identifier required')
        # FIXME: Sort out the context so it works
        self.context = self.messages = self.__parent__ = self.aq_inner = \
            messages
        self.groupInfo = groupInfo
        self.postId = self.__name__ = postId

    @Lazy
    def id(self):
        return self.postId

    @Lazy
    def post(self):
        '''The data for the post, as sucked out of the database

:raises ValueError: If the group ID and the site ID fail to match what
                    is in the database'''
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
        'The body of the post'
        retval = self.post['body']
        return retval

    @Lazy
    def files(self):
        '''The files attached to the post.

:returns: The files attached to the post
:rtype: A list of :class:`File` objects.'''
        retval = [File.from_query_dict(self.groupInfo, d)
                  for d in self.post['files_metadata']]
        return retval


class File(object):
    '''A file attached to a post.

:param groupInfo: The information about the current group.
:type groupInfo: Products.GSGroup.interfaces.IGSGroupInfo
:param str fileId: The file identifier.
:param str name: The file name.
:param int rawSize: The size of the file in bytes.
:param str mimeType: The MIME type of the file.'''
    def __init__(self, groupInfo, fileId, name, rawSize, mimeType):
        self.fileId = fileId
        #: The filename
        self.name = name
        self.rawSize = rawSize
        #: The human-readable size of the file
        self.size = self.format_size(rawSize)
        #: The MIME-type of the file.
        self.mimeType = mimeType
        u = '{0}/r/file/{1}/'
        #: The URL to the file (a short-link)
        self.url = u.format(groupInfo.siteInfo.url, fileId)

    @classmethod
    def from_query_dict(cls, groupInfo, d):
        '''Generate a file object from the dictionart that comes out of the
database.'''
        retval = cls(groupInfo, d['file_id'], d['file_name'],
                     d['file_size'], d['mime_type'])
        return retval

    @staticmethod
    def format_size(rawSize):
        '''Format the file size as a human-readable string

:param int rawSize: The size of the file in bytes.
:returns: A human readable size of the file.
:rtype: str'''
        if rawSize < 10**3:
            retval = '{0}b'.format(rawSize)
        elif 10**3 <= rawSize < (5 * 10**3):
            # If we are less than half a meg then the decimal point is
            # significant.
            retval = '{0:.1f}kb'.format((rawSize) / 10**3)
        elif (5 * 10**3) <= rawSize < 10**6:
            retval = '{0:.0f}kb'.format(rawSize / 10**3)
        elif 10**6 <= rawSize < 10**9:
            retval = '{0:.0f}mb'.format(rawSize / 10**6)
        elif 10**9 <= rawSize < 10**12:
            retval = '{0:.0f}gb'.format(rawSize / 10**9)
        else:
            retval = 'very big'
        return retval
