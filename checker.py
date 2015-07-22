#!/usr/bin/python

def main():
    from bs4 import BeautifulSoup
    import time,sys
    
    term, ccn = sys.argv[1], sys.argv[2]
    time = time.strftime("%X")
    r = requests.get('http://osoc.berkeley.edu/OSOC/osoc?p_term=%s&p_ccn=%s' % (term, ccn))
    soup = BeautifulSoup(r.text,'html.parser')    
    
    nums = soup.find(text=re.compile('^Limit:[0-9]+ Enrolled:[0-9]+ Waitlist:[0-9]+ Avail Seats:[0-9]+')).split(':')
    for i in range(len(nums)):
        if ':' in nums[i]:
            nums[i] = nums[i].split(':')[1]

    limit, enrolled, waitlist, avail = [int(num) for num in nums if num.isdigit()]
    
    
