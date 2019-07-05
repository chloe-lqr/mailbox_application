import os
from mail.signals import attachment_deal
from django.dispatch import receiver

@receiver(attachment_deal)
def attachment_process(sender, path_list, **args):

    for i in range(0, len(path_list[0])):
        #set your own path
        os.system("python D:\\mailbox\\repo_pledge.py %s" % path_list[0][i])
        print("repo_pledge done " + path_list[0][i])

    for i in range(0, len(path_list[1])):
        os.system("python D:\\mailbox\\bond_trade_summary.py %s" % path_list[1][i])
        print("bond_trade_summary done " + path_list[1][i])





