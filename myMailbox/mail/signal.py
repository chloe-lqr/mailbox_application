from django_mailbox.signals import message_received
from django.dispatch import receiver
import os
from django_mailbox.models import MessageAttachment
import re
from myMailbox import settings

@receiver(message_received)
def dance_jig(sender, message, **args):
    print("I just recieved a message titled %s from a mailbox named %s" % (message.subject, message.mailbox.name))
    instance = MessageAttachment.objects.filter(message_id=message.id)

    file_list = []
    for attachment in instance:
        file_list.append(attachment.get_filename())

    #deal with name
    path_list = file_rename(instance)

    for i in range(0, len(path_list[0])):
        #os.system("python D:\\mailbox\\repo_pledge.py %s" % path_list[0][i])
        print("repo_pledge done" + path_list[0][i])

    for i in range(0, len(path_list[1])):
        #os.system("python D:\\mailbox\\bond_trade_summary.py %s" % path_list[1][i])
        print("bond_trade_summary done" + path_list[1][i])



def file_rename(instance):
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    after_path_list = [[],[]]
    for attachment in instance:
        # print(attachment.get_filename())
        full_path = settings.MEDIA_ROOT + '\\' + str(attachment.document).replace('/', '\\')
        path_list = full_path.split('\\')
        path_list.pop(-1)
        path = '\\'.join(path_list)
        print(path)
        after_path = path + '\\' + str(attachment.id) + '+' + attachment.get_filename()
        if os.path.exists(full_path):
            os.rename(full_path, after_path)
        if re.match('.*质押式回购市场交易情况总结日报.*', attachment.get_filename()) != None:
            after_path_list[0].append(after_path)
        elif re.match('.*现券市场交易情况总结日报.*', attachment.get_filename()) != None:
            after_path_list[1].append(after_path)
    print(after_path_list)
    return after_path_list
