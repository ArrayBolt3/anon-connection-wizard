#!/usr/bin/python3 -u

import fileinput, os, shutil


'''repair_torrc() function will be called when we want to gurantee the existence of:
1. /etc/tor/torrc file
2. /etc/tor/torrc.anondist file
3. /etc/tor/torrc is exactly the same with /etc/tor/torrc.anondist
4. /etc/tor/torrc.d/95_whonix.torrc
'''
def repair_torrc():
    repair_torrc_d()
    repair_torrc_anondist()
    shutil.copyfile('/etc/tor/torrc.anondist', '/etc/tor/torrc')
    repair_torrc_95_whonix()


'''repair_torrc_d() will gurantee the existence of /etc/torrc.d and /usr/local/etc/torrc.d/
'''
def repair_torrc_d():
    if not os.path.exists('/etc/torrc.d/'):
        os.makedirs('/etc/torrc.d/')
    if not os.path.exists('/usr/local/etc/torrc.d/'):
        os.makedirs('/usr/local/etc/torrc.d/')

'''repair_torrc_anondist() will gurantee the existence of /etc/tor/torrc.anondist
However, maintainer need to manually update its content when
any changes is made to  /etc/tor/torrc.anondist
'''
def repair_torrc_anondist():
    with open('/etc/tor/torrc.anondist', "w+") as f:
        f.write("\
## Do not edit this file!\n\
## Add modifications to the following file instead:\n\
## /usr/local/etc/torrc.d/50_user.torrc\n\
\n\
%include /etc/torrc.d\n")


'''repair_torrc_95_whonix() will gurantee the existence of /etc/torrc.d/95_whonix.torrc
However, maintainer need to manually update its content when
any changes is made to  /etc/torrc.d/95_whonix.torrc
'''
def repair_torrc_95_whonix():
    repair_torrc_d()
    with open('/etc/torrc.d/95_whonix.torrc', "w+") as f:
        f.write("\
## Do not edit this file!\n\
## Add modifications to the following file instead:\n\
## /usr/local/etc/torrc.d/50_user.torrc\n\
\n\
%include /usr/local/etc/torrc.d\n")
