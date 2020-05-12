#! python3
'一个密码保管程序'
import sys,pyperclip
password = {'email':'baby_CAT.123434',
            'wecat':'YUAN.yuan.123434',
            'blog':'lijunfenghaoshuai233'
            }
if len(sys.argv) < 2:
    print('Usage:python project_password.py' + \
          ' [account] - copy account password.')
    sys.exit()
account = sys.argv[1] # arg账户名

if account in password:
    pyperclip.copy(password[account])
    print('Password for',account,'copied to clipboard.')
else:
    print('There is no account named',account,'.')


