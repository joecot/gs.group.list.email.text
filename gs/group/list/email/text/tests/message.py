# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import, unicode_literals, print_function, division
from email.mime.text import MIMEText
from mock import patch
from unittest import TestCase
from gs.group.list.email.text.message import TextMessagePart


class TextMessagePartTest(TestCase):
    @staticmethod
    def text():
        return 'This is some text'

    @patch('gs.group.list.email.text.message.getMultiAdapter')
    def test_as_email(self, m_gma):
        m_gma.return_value = self.text
        tmp = TextMessagePart(None, None)
        r = tmp.as_email()

        self.assertIsInstance(r, MIMEText)
        self.assertIn('text/plain', r['Content-type'])
