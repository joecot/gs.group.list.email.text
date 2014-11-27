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

    def post(self, post_id):
        """ Retrieve a particular post.

            Returns:
                {'post_id': ID, 'group_id': ID, 'site_id': ID,
                 'subject': String,
                 'date': Date, 'author_id': ID,
                 'body': Text, 'hidden': DateOrNull,
                 'files_metadata': [Metadata]
                 }
             or
                None"""
        pt = self.postTable
        statement = pt.select()
        statement.append_whereclause(pt.c.post_id == post_id)

        session = getSession()
        r = session.execute(statement)
        retval = None
        if r.rowcount:
            assert r.rowcount == 1, "Posts should always be unique"
            row = r.fetchone()
            retval = {k: v for k, v in list(row.items())}
            retval['files_metadata'] = self.files_metadata(row['post_id'])
        return retval

    def files_metadata(self, postId):
        """ Retrieve the metadata of all files associated with this post.

            Returns:
                {'file_id': ID, 'mime_type': String,
                 'file_name': String, 'file_size': Int}
             or
                []

        """
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
