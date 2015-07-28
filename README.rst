============================
``gs.group.list.email.text``
============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The plain-text version of the messages from a GroupServer group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-11-27
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

.. _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

The email messages that GroupServer sends from a group are
different from what is received. This product supplies the code
for representing the plain-text version of a message, and an
adaptor for connecting it to the rest of GroupServer [#adaptor]_.

The headers are changed when the message is being sent
[#sender]_, while the HTML version of the message is currently
dropped.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.list.email.text
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#adaptor] See the ``gs.group.list.email.base`` product
             <https://github.com/groupserver/gs.group.list.email.base>

.. [#sender] See the ``gs.group.list.sender`` product
             <https://github.com/groupserver/gs.group.list.sender>

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

..  LocalWords:  IAppendix viewlets groupserver EmailTextPrologue
