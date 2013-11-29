#!/usr/bin/python
def main():
    import urllib2, smtplib, time
    import send, popup
    
    url = urllib2.urlopen('http://osoc.berkeley.edu/OSOC/osoc?p_term=SP&p_ccn=22507')
    html = url.read()
    
    i = 0
    while i < len(html)-1:
        if html[i:i+9] == 'Waitlist:':
            waitlist = html[i+9:i+11]
            break
        i+=1
        
    waitlist = int(waitlist)
    
    if waitlist < 35:
        popup.showNotification(100,"ALERT: Sign up for Telebears Waitlist now! \n" + "The number of waitlists is now "+str(waitlist)+". The CCN is 22507")
        return time.asctime(time.localtime())
    return 0



































#send.sendemail(from_addr    = 'Xtremeaznkid@gmail.com', 
#               to_addr_list = ['Xtremeaznkid@gmail.com'],
#               cc_addr_list = ['Xtremeaznkid@gmail.com'], 
#               subject      = 'Telebears alert', 
#               message      = 'The waitlist for the class you created an alert for is no longer full. Please register now. (CCN = 22507)', 
#               login        = '', 
#               password     = '')
