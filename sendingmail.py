# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:08:33 2023

@author: selen
"""

import smtplib
s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login("sender mail", "password")
message = "your message"
while True:
    s.sendmail("sender mail", "receiver", message)
    s.quit()