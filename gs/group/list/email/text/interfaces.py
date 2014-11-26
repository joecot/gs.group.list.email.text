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
from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class ITextMessage(IViewletManager):
    'The viewlet manager for the entire Text version of the email message'


class IPrologue(IViewletManager):
    'The viewlet manger for the prologue of the message'


class IBody(IViewletManager):
    'The viewlet manger for the body of the message'


class IAppendix(IViewletManager):
    'The viewlet manger for the appendix of the message'


class IPost(Interface):
    'A marker interface for a post'
