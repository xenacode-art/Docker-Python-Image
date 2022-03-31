# Python code to auto delete mails from my gmail account.
import imaplib
from getpass import getpass
import email
from email.header import decode_header

# Input account details
username = input("Enter Your Mail Address: ")
password = getpass(("Input Password: "))

# Creating an IMP4 for connection via ssl

imap = imaplib.IMAP4_SSL("imap.gmail.com")
# Authentication
imap.login(username, password)
# Select mail box you want to delete
# if you want to delete Spam, use
# imap.select("SPAM")
# imap.list()
# search for specific mails by sender
# status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')
imap.select("INBOX")

# search for specific mails to delete
# to get mails after a specific date
# status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
# to get mails before a specific date
# imap.list()
status, messages = imap.search(None, 'BEFORE "01-MAR-2022"')
# status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')
# status, messages = imap.search(None, 'FROM "ALL"')

# convert messages to a list of email IDs
messages = messages[0].split(b' ')
for mail in messages:
     _, msg = imap.fetch(mail, "(RFC822)")
   # you can delete the for loop for #performance if you have a long list of emails
  #  because it is only for printing the #SUBJECT of target email to delete
     for response in msg:
        if isinstance(response, tuple):
             msg = email.message_from_bytes(response[1])
       #     decode the email subject
        subject = decode_header(msg["Subject"])[0][0]
     if isinstance(subject, bytes):
   #             if it's a bytes type, decode to str
                 subject = subject.decode()
     print("Deleting", subject)
   # mark the mail as deleted
     imap.store(mail, "+FLAGS", "\\Deleted")
