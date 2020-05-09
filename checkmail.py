import imapclient,pyzmail


# emailId = input('Enter your email : ')
# password = input('Enter enter your password : ')
# print(emailId)
# print(password)

user=imapclient.IMAPClient('imap.gmail.com',993,ssl=True,)

user.login('jayonet19@gmail.com','freak@321')
print(user.login_status)
user.select_folder('INBOX',readonly=True)

search = input('enter the search for mail : ')
UIDs=user.search([search])
print(UIDs)

user.logout()