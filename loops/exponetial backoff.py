max_retries=5
attempts=0
wait_time=1


while attempts < max_retries:
      print("Atempts",attempts, "-","Wait Time",wait_time) 
      attempts+=1
      wait_time *=2

print("Finish...")      