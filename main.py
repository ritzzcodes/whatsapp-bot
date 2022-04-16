import pywhatkit
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter mobile number of Receiver : ')
message = input('Enter Message: ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(mobile,message,hour,minute)
