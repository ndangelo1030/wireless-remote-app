#channel guide
import channeldict from channeldict

def channelguide():
  for d in channeldict:
	  print(d)
  #shows all tv networks

for a,b in channeldict.items():
    print("Channel : {0}, Network : {1}".format(a,b))
  #shows all tv networks with their channel numbers

#end program
