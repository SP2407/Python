#-#-# Sending Email using python Script #-#-#

import emails
message = emails.html(html="<p>Hi!<br>Here is your receipt...",
                          subject="Your receipt No. 567098123",
                          mail_from=('Some Store', 'store@somestore.com'))

mail_py=message.send(to='pawarsaurabhsp96@gmail.com',
                     smtp={'host':'smtp.gamil.com',
                           'timeout':5,
                           'port':587,
                           'user':'pawarsaurabhssp96@gmail.com',
                           'password':'@Saurabhsp96#',
                           'tls':True})

print(mail_py.status_code)