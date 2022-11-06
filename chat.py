from datetime import datetime
from pytz import timezone
logfile='chat.txt'


def getchat():
  fullchat=[]
  with open(logfile) as f:
    for line in f:
      line=line.rstrip('\n\r')
      record={'message':line}
      fullchat.append(record)
  return fullchat

  
def add_message(message):
  tzone = timezone('America/New_York')
  time = datetime.now(tzone).strftime("%-I:%M%p ")
  with open(logfile,'a') as f:
    if message != "":
      f.write(time + "Anonymous: "+ message + '\n' )
  return None