import sys
if len(sys.argv) == 2:
  script_name=sys.argv[0]
  temp = float(sys.argv[1])
else:
  script_name=sys.argv[0]
  temp = 15

if(temp<15):
  alert="COLD"
elif (temp<=30):
  alert="NORMAL"
elif (temp>30):
  alert ="HOT"

print("Temparature : ",temp)
print("Alert : ",alert)
