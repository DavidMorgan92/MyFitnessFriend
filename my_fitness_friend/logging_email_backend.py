import django.core.mail.backends.smtp
import logging

# or you could enter a specific logger name
logger = logging.getLogger(__name__)

# https://stackoverflow.com/a/37683078


class LoggingEmailBackend(django.core.mail.backends.smtp.EmailBackend):
    def send_messages(self, email_messages):
        try:
            for msg in email_messages:
                logger.info(u"Sending message '%s' to recipients: %s",
                            msg.subject, msg.to)
        except:
            logger.exception("Problem logging recipients, ignoring")

        return super(LoggingEmailBackend, self).send_messages(email_messages)
