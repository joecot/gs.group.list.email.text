Adaptor
=======

.. currentmodule:: gs.group.list.email.text

The :class:`message.TextMessagePart` class adapts a post (as the
context) and a browser request, and provides the
:class:`gs.group.list.email.base.interfaces.IMessagePart`
interface.

The :meth:`message.TextMessagePart.as_email` method returns an
instance of the standard :class:`email.mime.text.MIMEText` class,
with the MIME-type set to :mimetype:`text/plain`. The UTF-8
character-encoding is set.
