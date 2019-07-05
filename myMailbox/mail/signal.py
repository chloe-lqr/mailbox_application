from django_mailbox.signals import message_received
from django.dispatch import receiver
from django_mailbox.models import MessageAttachment
import re
from myMailbox import settings
from mail.signals import attachment_deal
import os

@receiver(message_received)
def dance_jig(sender, message, **args):
    print("I just recieved a message titled %s from a mailbox named %s" % (message.subject, message.mailbox.name))
    instance = MessageAttachment.objects.filter(message_id=message.id)

    file_list = []
    for attachment in instance:
        file_list.append(attachment.get_filename())

    path_list = file_classify(instance)
    attachment_deal.send(sender = sender, path_list = path_list)


def file_classify(instance):
    after_path_list = [[], []]
    for attachment in instance:
        full_path = settings.MEDIA_ROOT + '\\' + str(attachment.document).replace('/', '\\')
        if os.path.exists(full_path):
            if re.match('.*质押式回购市场交易情况总结日报.*', attachment.get_filename()) != None:
                after_path_list[0].append(full_path)
            elif re.match('.*现券市场交易情况总结日报.*', attachment.get_filename()) != None:
                after_path_list[1].append(full_path)
    print(after_path_list)
    return after_path_list