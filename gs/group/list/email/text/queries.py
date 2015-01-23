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
from gs.core import to_unicode_or_bust
from gs.database import getTable, getSession


class MessageQuery(object):
    def __init__(self, context):
        self.context = context
        self.postTable = getTable('post')
        self.fileTable = getTable('file')

    def post(self, postId):
        """Retrieve a post

:param str post_id: The identifier of a post
:returns: The post for the ID, or ``None``
:rtype: dict

The dictionary representing the post contains the following

==================  ========  ==========================
Key                 Type      Note
==================  ========  ==========================
``post_id``         str       The post identifier
``group_id``        str       The group identifier
``site_id'          str       The site identifier
``subject``         str       The subject (topic title)
``date``            DateTime  The date the post was made
``author_id``       str       The author identifier
``body``            str       The body of the post
``hidden``          DateTime  Set if the post is hidden
``files_metadata``  ``list``  The list of attached files
==================  ========  ==========================
"""
        if not postId:
            raise ValueError('postId must be set')

        pt = self.postTable
        statement = pt.select()
        statement.append_whereclause(pt.c.post_id == postId)

        session = getSession()
        r = session.execute(statement)
        retval = None
        if r.rowcount:
            assert r.rowcount == 1, "Posts should always be unique"
            row = r.fetchone()
            retval = {k: v for k, v in list(row.items())}
            fm = []
            if retval['has_attachments']:
                fm = self.files_metadata(row['post_id'])
            retval['files_metadata'] = fm

        # assert postId == retval['post_id'], 'post_id missmatch'
        return retval

    def files_metadata(self, postId):
        """Retrieve the metadata of all files associated with this post."""
        ft = self.fileTable
        statement = ft.select()
        statement.append_whereclause(ft.c.post_id == postId)

        session = getSession()
        r = session.execute(statement)
        retval = [{
            'file_id': row['file_id'],
            'file_name': to_unicode_or_bust(row['file_name']),
            'date': row['date'],
            'mime_type': to_unicode_or_bust(row['mime_type']),
            'file_size': row['file_size'], } for row in r]
        return retval
