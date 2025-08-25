n=4
rooms=[0]*n
for i in range(n):
  x=int(input("Enter 1 for dirty, 0 for clean : "))
  rooms[i]=x
initial_state=int(input("Enter the initial state(0-3) : "))
while True:
  action=int(input("Enter 0 for sucking, 1 for moving left, 2 for moving right :"))
  if action==0:
    rooms[initial_state]=0
    print(f"Sucking the dust in room {initial_state}")
    print(f"0 : {rooms[0]}" ,f",1 : {rooms[1]}",f",2: {rooms[2]}" ,f",3 : {rooms[3]}")
  elif action==1:
    initial_state-=1 if initial_state>0 else 0
    print(f"Moving to room {initial_state}")
    print(f"0 : {rooms[0]}" ,f",1 : {rooms[1]}",f",2: {rooms[2]}" ,f",3 : {rooms[3]}")
  elif action==2:
    initial_state+=1 if initial_state<n-1 else n-1
    print(f"Moving to room {initial_state}")
    print(f"0 : {rooms[0]}" ,f",1 : {rooms[1]}",f",2: {rooms[2]}" ,f",3 : {rooms[3]}")
  else:
    print("Invalid action")
    continue
  print(rooms)
  if sum(rooms)==0:
    print("All rooms clean")
    break
