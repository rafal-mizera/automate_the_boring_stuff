import smtplib
import imapclient

imap_obj = imapclient.IMAPClient("imap.gmail.com",ssl=True)
imap_obj.login("kontodonaukiprogramowania123@gmail.com","Python123")


