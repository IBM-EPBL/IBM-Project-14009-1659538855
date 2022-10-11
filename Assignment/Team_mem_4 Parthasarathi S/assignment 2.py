import random
tem=random.uniform(0,50)
hum=random.uniform(0,50)
print("Temperature sensed:",tem)
print("Humidity sensed:",hum)
thersT=30
thersH=60
if tem>thersT and hum>thersH:
    print("High Temperature Measured!!...")
