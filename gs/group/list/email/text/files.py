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
from .viewlet import EmailMessageViewlet


class FilesViewlet(EmailMessageViewlet):
    'Base class for the three file viewlets'

    @Lazy
    def files(self):
        retval = self.context.files
        return retval

    @Lazy
    def n(self):
        retval = len(self.files)
        return retval


class FileNotice(FilesViewlet):
    'The viewlet for the file-notice in the prologue'
    @Lazy
    def show(self):
        retval = self.n == 1
        return retval


class FilesNotice(FilesViewlet):
    'The viewlet for the files-notice (note the plural) in the prologue'
    @Lazy
    def show(self):
        retval = self.n > 1
        return retval


class Files(FilesViewlet):
    'The list of files in the appendix'
    @Lazy
    def show(self):
        retval = self.n > 0
        return retval
