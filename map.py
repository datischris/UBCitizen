logfile='data.txt'

def getcoords():
  fullchat=[]
  with open(logfile) as f:
    for line in f:
      line=line.rstrip('\n\r')
      record={'latlong':line}
      fullchat.append(record)
  return fullchat

def add_coords(message):
  if message:
    with open(logfile,'a') as f:
      f.write(message+'\n')
  return None