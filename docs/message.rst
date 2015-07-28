Message template
================

The *page* ``text`` is registered against the base
``gs-group-list-email`` traversal. It takes the post-identifier
off the URL and returns a rendered page:
<http://groupserver.org/groups/development/messages/gs-group-list-email/N5o9zxaSkSYFQBB45HqHV/text>


The message template itself just contains the
``groupserver.EmailTextMessage`` viewlet manager [#viewlet]_ —
which provides the
:class:`gs.group.list.email.text.interfaces.ITextMessage`
interface. By default, three viewlets are provided for the
message. Each viewlet contains further viewlet manager,
effectively dividing the message in three: the prologue_, the
body_ and the appendix_.

.. code-block:: none

  ┌─Text message───────────────────────────────────────────┐
  │                                                        │
  │ ┌─Text message viewlet manager───────────────────────┐ │
  │ │ gs.group.list.email.text.interfaces.ITextMessage   │ │
  │ │                                                    │ │
  │ │ ┌─Prologue viewlet manager───────────────────────┐ │ │
  │ │ │ gs.group.list.email.text.interfaces.IPrologue  │ │ │
  │ │ └────────────────────────────────────────────────┘ │ │
  │ │                                                    │ │
  │ │ ┌─Body viewlet manager───────────────────────────┐ │ │
  │ │ │ gs.group.list.email.text.interfaces.IBody      │ │ │
  │ │ └────────────────────────────────────────────────┘ │ │
  │ │                                                    │ │
  │ │ ┌─Appendix viewlet manager───────────────────────┐ │ │
  │ │ │ gs.group.list.email.text.interfaces.IAppendix  │ │ │
  │ │ └────────────────────────────────────────────────┘ │ │
  │ │                                                    │ │
  │ └────────────────────────────────────────────────────┘ │
  │                                                        │
  └────────────────────────────────────────────────────────┘

.. note:: The default GroupServer viewlets make liberal use of
          Unicode characters. As such it is necessary to use
          UTF-8 encoding for the messages, and they may fail to
          render correctly if only ASCII is used.

Prologue
--------

The prologue of a message appears at the top of the message body,
but before the body_ proper. The *viewlet manager*
``groupserver.EmailTextPrologue``
(:class:`gs.group.list.email.text.interfaces.IPrologue`) is
normally filled by the *File notice* viewlets.

The *File notice* viewlets state that there is one or more files
listed in the appendix_:

* One (``gs-group-list-email-text-prologue-file``) provides a
  short notice that there is *a* file listed in the appendix of a
  message,

* The other (``gs-group-list-email-text-prologue-files``)
  provides a short notice that there are *multiple* files listed
  in the appendix of a message.

.. note:: Two viewlets are provided because it makes localisation
          easier.

Body
----

The *body* of the message is provided by the
``groupserver.EmailTextBody``
(:class:`gs.group.list.email.text.interfaces.IBody`) viewlet
manager.

The *Plan body* (``gs-group-list-email-text-body-plain``) viewlet
writes out the body of the post much as it was when it was sent
in.

Appendix
--------

The *appendix* of the message is provided by the
``groupserver.EmailTextAppendix``
(:class:`gs.group.list.email.text.interfaces.IAppendix`) viewlet
manager. Two viewlets are provided as standard: a `files list`_
and a footer_.

Files list
~~~~~~~~~~

Files are large burden for a list, as they dramatically increase
the size of the message for little gain [#picture]_. Because of
this the attached files are replaced with *links* to the files on
the Web. The *Files list* viewlet
(``gs-group-list-email-text-appendix-files``) provides this list.

Footer
~~~~~~

The standard *Footer* viewlet
(``gs-group-list-email-text-appendix-footer``) provides the
following:

* The *Unsubscribe* link, which is legally required in many
  jurisdictions.
* A link to the topic on the Web.

.. [#viewlet] See the ``zope.viewlet`` product
              <https://pypi.python.org/pypi/zope.viewlet/>

.. [#picture] If “a picture can speak a thousand words” then
              represent that concept with a picture. Send
              attempts that are less than 2K (the size of a
              thousand words, compressed) to
              <mpj17@onlinegroups.net>.
