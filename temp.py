d_c = {}
d_b = {}
d_a = {}
d_b_1 = {}
d_p = {}
process_sno = [1,2,3,4,5]

n = len(process_sno)

t_a_t = [-1]*n  # Intializing a list of n elements

waiting_time = [-1]*n # Intializing a list of n elements
    
arrival = [1,2,2,3,3]
	
burst_time = [5,9,8,13,11]

priority = [3,4,2,1,5]

rq = []

completed = []

for i in range(n):
    
    d_a[i+1] = arrival[i]
    
    d_b[i+1] = priority[i]
    
    d_c[i+1] = 0
    
    d_b_1[burst_time[i]] = i+1
    
    d_p[priority[i]] = burst_time[i]

ready_queue = []

dit = {}

visited = []

count = 1

for i in range(n):
    
    if i+1 not in visited and count >= d_a[i+1]:
        visited.append(i+1)
        ready_queue.append(d_b[i+1]) 
        rq.append(i+1)
        
while ready_queue:

    print(ready_queue)
    
    m = min(ready_queue)
    
    idx = ready_queue.index(m)
    
    
    process_number = rq[idx]
    
    ready_queue.remove(m)
    
    rq.pop(idx)
    
    if d_p[m] <= 1:
        
        if completed and d_c[completed[-1]] != 0:
            
            d_c[process_number] = count + 1
            
        else:
            
            
            
            d_c[process_number] = count + 1
            
        completed.append(process_number)
        
        count = d_c[process_number]
        
    else:
        
        count += 1
        
        d_p[process_number] -= 1 
        
    
    
    for i in range(n):
    
        if i+1 not in visited and count >= d_a[i+1]:
            
            visited.append(i+1)
            
            ready_queue.append(d_b[i+1]) 
            
            rq.append(i+1)
        
    if process_number not in completed:
        
        ready_queue.append(d_b[process_number])
        
        rq.append(process_number)
        
    
    

# Turn Around Time Computation

for i in range(n):
    
    t_a_t[i] = d_c[i+1] - d_a[i+1]
    

# Waiting Time Computation.  WT = TAT - BT
    
for i in range(n):
    
    waiting_time[i] = t_a_t[i] - burst_time[i]
    


print ("{:<16} {:<16} {:<16} {:<16}{:<16} {:<18}".format("Process No.","Arrival Time","Burst Time","complete Time","Turn Around Time","Waiting Time"))

for i in range(1,n):
    
    print ("{:<16} {:<16} {:<16} {:<16}{:<16} {:<18}".format(i,arrival[i],burst_time[i],d_c[i],t_a_t[i],waiting_time[i]))

Average_waiting_time = sum(waiting_time) / n

Average_turnaround_time = sum(t_a_t) / n
        
print("\n")

print("Average Turnaround Time: ",Average_turnaround_time)

print("Average Waiting Time: ",Average_waiting_time)
 

