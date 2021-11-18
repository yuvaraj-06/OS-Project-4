# Create your views here.
from django.shortcuts import render


def home(request):
    
    

    return render(request,'Main-page.html')

def index(request):
    
    d= {'FCFS': 'FCFS (First Come First Serve)','SRTF':'SRTF,Shortest Remaining Time First (Preemtive)',"RR":"Round Robin (Preemtive)","SRJFRR":"SRJFRR"}


    
    
    c={'d':d}
    '''
    res = {
        "data" : [[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6]],
    }

    return render(request,'home.html',res)
    '''

    return render(request,'home.html',c)
    
def add(request):
    a=(request.POST['a']).split()
    b=(request.POST['b']).split()
    
    d=int((request.POST['d']))
    e=(request.POST['lan'])
    

    for i in range(len(a)):

        a[i] = int(a[i])

        b[i] = int(b[i])

       


    arrival = a
            
    burst_time = b

    

    quantum_time = d

    n = len(a)

    gantt = []

    if e == 'FCFS':

        
        # FCFS Scheduling
        
        d_c = {} # Completion time
        d_b = {} # Burst time
        d_a = {} # Arrival time
        

        process_sno = [i for i in range(1,n+1)] # Storing each process number

        t_a_t = [-1]*n  # Intializing a list of n element 

        waiting_time = [-1]*n # Intializing a list of n elements


        completed = [] 

        gantt = []


        # Sorting the arrival time using bubble sort.

        for i in range(n-1):
            
                for j in range(0, n-i-1):
                    
                    if arrival[j] > arrival[j + 1] :
                        
                        arrival[j], arrival[j + 1] = arrival[j + 1], arrival[j]
                        
                        process_sno[j],process_sno[j+1] = process_sno[j+1],process_sno[j] 
                        
                        burst_time[j],burst_time[j+1] = burst_time[j+1],burst_time[j]




        for i in range(n):
            
            d_a[i+1] = arrival[i] # Key = process number , Value = arrival time of that particular process
            
            d_b[i+1] = burst_time[i] # Key = process number , Value = arrival time of that particular process
            
            d_c[i+1] = 0 # Key = process number , Value = arrival time of that particular process
            
            

        ready_queue = [] # A ready_queue list  is used to store that burst times of the processes. 
        
        visited = [] # The element is add to the visited list.
        count = 0 # Time

        for i in range(n):
            
            if i+1 not in visited and count >= d_a[i+1]: # A condition checking whether the current time is greater than the arrival time of the process.
                visited.append(i+1)  # The element is add to the visited list.
                ready_queue.append(i+1) # The corresponding process number is add to this list
                
        while ready_queue: # Condition if ready queue is empty or not.
            
            m = ready_queue.pop(0) # The process is taken on the FCFS basis.
            
            process_number = m 

            b_time = d_b[m] # Burst time of process
            
            
                
            
                    
            d_c[process_number] = count + d_b[m]  # Completion time calculation
            
            count = d_c[process_number] # Update the current time
                
            
            
            for i in range(n):
            
                if i+1 not in visited and count >= d_a[i+1]: # A condition checking whether the current time is greater than the arrival time of the process.
                    visited.append(i+1)  # The element is add to the visited list.
                    ready_queue.append(i+1) # The corresponding process number is add to this list
                    
            
        gantt = process_sno # gantt chart

        # Turn Around Time.

        for i in range(n):
            
            t_a_t[i] = d_c[i+1] - d_a[i+1]

        # Burst Time.

        for i in range(n):
            
            waiting_time[i] = t_a_t[i] - burst_time[i]
            
        Average_waiting_time = sum(waiting_time) / n

        Average_turnaround_time = sum(t_a_t) / n







        


    elif e == "SRTF":

        d_c = {} # Completion time
        d_b = {} # Burst time
        d_a = {} # Arrival time
        

        process_sno = [i for i in range(1,n+1)] # Storing each process number

        t_a_t = [-1]*n  # Intializing a list of n element 

        waiting_time = [-1]*n # Intializing a list of n elements

        completed = [] # Initializing a list that is used to tell which processes are completed 


        for i in range(n): # A loop for storing arrival , burst times and process numbers in the form of key value pairs.
            
            d_a[i+1] = arrival[i] # Key = process number , Value = arrival time of that particular process
            
            d_b[i+1] = burst_time[i] # Key = process number , Value = arrival time of that particular process
            
            d_c[i+1] = 0 # Key = process number , Value = arrival time of that particular process

        ready_queue = [] # A ready_queue list  is used to store that burst times of the processes. 

        rq = [] # A similar queue to ready queue to store the particular process number for all the queue 

    
        visited = [] # A list of all the visited processes.

        count = 0 # Time

        for i in range(n):
            
            if i+1 not in visited and count >= d_a[i+1]:  # A condition checking whether the current time is greater than the arrival time of the process.

                visited.append(i+1) # The element is add to the visited list.
                ready_queue.append(d_b[i+1]) # The burst time of the process in appended to the ready queue.
                rq.append(i+1) # The corresponding process number is add to this list
                
        while ready_queue: # Condition if ready queue is empty or not.
            
            m = min(ready_queue) # The process having the minimum burst time is found.
            
            idx = ready_queue.index(m) # Index of the minimum burst time process is computed.
            
            
            process_number = rq[idx] # Corresponding process number is stored in this variable using the index that is found.

            ready_queue.remove(m) # The process's burst time is removed from the ready queue.
            
            rq.pop(idx) # The corresponding process number is removed from this list.
            
            if m <= 1: # m = burst time of process , if the burst time is less than or equal to 1 , then the process is said to be completed.                                                                                                                                   

                
                    
                    
                    
                d_c[process_number] = count + 1 # Count = Time , The time when the process is completed is stored in the d_c dictionary.
                    
                completed.append(process_number) # Process number is added to the completed list
                
                count = d_c[process_number] # Update the time  
                
            else:
                
                count += 1  # Update the time 
                
                d_b[process_number] -= 1 # Update the burst time of the process
                
            
            
            for i in range(n):
            
                if i+1 not in visited and count >= d_a[i+1]:  # A condition checking whether the current time is greater than the arrival time of the process.
                    
                    visited.append(i+1) # The element is add to the visited list.
                    
                    ready_queue.append(d_b[i+1]) # The burst time of the process in appended to the ready queue.
                    
                    rq.append(i+1) # The corresponding process number is add to this list
                
            if process_number not in completed:  # If the process is not completed, it is again added to the ready queue.
                
                ready_queue.append(d_b[process_number]) # Adding the updated burst time of the particular process to the ready queue.
                
                rq.append(process_number) # Adding the process number.

            if not gantt or gantt[-1] != process_number: # if the previous process is also the same process that is being executed now, then there is not need of duplicates.

                gantt.append(process_number) # Adding the process to the gantt chart for displaying purposes.

        # Turn Around Time Computation TAT = CT - AT
        for i in range(n):
            
            t_a_t[i] = d_c[i+1] - d_a[i+1]

        # Waiting Time Computation.  WT = TAT - BT
        for i in range(n):
            
            waiting_time[i] = t_a_t[i] - burst_time[i]
            
        Average_waiting_time = sum(waiting_time) / n

        Average_turnaround_time = sum(t_a_t) / n

        

        pass


    

    elif e == "RR":

        
        d_c = {} # Completion time
        d_b = {} # Burst time
        d_a = {} # Arrival time
        
        process_sno = [i for i in range(1,n+1)] # Storing each process number


        t_a_t = [-1]*n  # Intializing a list of n element

        waiting_time = [-1]*n # Intializing a list of n elements

        completed = [] # Initializing a list that is used to tell which processes are completed 

        for i in range(n): # A loop for storing arrival , burst times and process numbers in the form of key value pairs.
            
            d_a[i+1] = arrival[i] # Key = process number , Value = arrival time of that particular process
            
            d_b[i+1] = burst_time[i] # Key = process number , Value = arrival time of that particular process
            
            d_c[i+1] = 0 # Key = process number , Value = arrival time of that particular process
            
            

        ready_queue = [] # A ready_queue list  is used to store that burst times of the processes. 
       
        visited = []  # A list of all the visited processes.
        count = 0# Time

        for i in range(n):
            
            if i+1 not in visited and count >= d_a[i+1]: # A condition checking whether the current time is greater than the arrival time of the process.
                visited.append(i+1) # The element is add to the visited list.
                ready_queue.append(i+1) # The corresponding process number is add to this list
                
        while ready_queue: # Condition if ready queue is empty or not.
            
            m = ready_queue.pop(0) # The process is taken on the FCFS basis.
            
            process_number = m # Process number.

            b_time = d_b[process_number] # Burst time of the process based on the process number.
            
            if b_time <= quantum_time: # Checks if the burst time is less than or equal to the quantum time.
                
                
                    
                d_c[process_number] = count + b_time # Count = Time , The time when the process is completed is stored in the d_c dictionary.
                    
                completed.append(process_number) # Process number is added to the completed list
                
                count = d_c[process_number] # Update the time  
                
            else:
                
                count += quantum_time # Update the time 
                
                d_b[m] -= quantum_time # Update the burst time of the process
            
            for i in range(n):
            
                if i+1 not in visited and count >= d_a[i+1]: # A condition checking whether the current time is greater than the arrival time of the process.
                    visited.append(i+1)  # The element is add to the visited list.
                    ready_queue.append(i+1) # The corresponding process number is add to this list
                
            if process_number not in completed:  # If the process is not completed, it is again added to the ready queue.
                
                ready_queue.append(process_number) # Adding the updated burst time of the particular process to the ready queue.

            if not gantt or gantt[-1] != process_number: # if the previous process is also the same process that is being executed now, then there is not need of duplicates.

                gantt.append(process_number) # Adding the process to the gantt chart for displaying purposes.


        # Turn Around Time Computation
        for i in range(n):
            
            t_a_t[i] = d_c[i+1] - d_a[i+1] 

        # Waiting Time Computation.  WT = TAT - BT
        for i in range(n):
            
            waiting_time[i] = t_a_t[i] - burst_time[i]
            
        Average_waiting_time = sum(waiting_time) / n

        Average_turnaround_time = sum(t_a_t) / n

        pass

    elif e == "SRJFRR":

        

        d_c = {} # Completion time
        d_b = {} # Burst time
        d_a = {} # Arrival time

        process_sno = [i for i in range(1,n+1)] # Storing each process number

        t_a_t = [-1]*n  # Intializing a list of n element

        waiting_time = [-1]*n # Intializing a list of n elements

        completed = [] # Initializing a list that is used to tell which processes are completed 

        for i in range(n):  # A loop for storing arrival , burst times and process numbers in the form of key value pairs.
            
            d_a[i+1] = arrival[i] # Key = process number , Value = arrival time of that particular process
            
            d_b[i+1] = burst_time[i] # Key = process number , Value = arrival time of that particular process
            
            d_c[i+1] = 0 # Key = process number , Value = arrival time of that particular process
            
            

        ready_queue = []  # A ready_queue list  is used to store that burst times of the processes. 
 
        rq = [] # A similar queue to ready queue to store the particular process number for all the queue 
        
        visited = []  # A list of all the visited processes.
        count = 0# Time


        for i in range(n):
            
            if i+1 not in visited and count >= d_a[i+1]: # A condition checking whether the current time is greater than the arrival time of the process.
                visited.append(i+1) # The element is add to the visited list.
                ready_queue.append(d_b[i+1]) # The corresponding process number is add to this list
                
                rq.append(i+1)  # The corresponding process number is add to this list
                
        while ready_queue:  # Condition if ready queue is empty or not.
            
            m = min(ready_queue) # The process having the minimum burst time is found.
            
            idx = ready_queue.index(m) # Index of the minimum burst time process is computed.
            
            process_number = rq[idx] # Corresponding process number is stored in this variable using the index that is found.
            
            ready_queue.remove(m) # The process's burst time is removed from the ready queue.
            
            rq.pop(idx) # The corresponding process number is removed from this list.
            
            
            if m <= quantum_time: # m = burst time of process , if the burst time is less than or equal to 1 , then the process is said to be completed.         
                
                
                    
                    
                    
                d_c[process_number] = count + d_b[process_number] # Count = Time , The time when the process is completed is stored in the d_c dictionary.
                    
                completed.append(process_number) # Process number is added to the completed list
                
                count = d_c[process_number]  # Update the time  
                
            else:
                
                count += quantum_time # Update the time  
                
                d_b[process_number] -= quantum_time  # Update the burst time of the process
                
            
            
            for i in range(n):
            
                if i+1 not in visited and count >= d_a[i+1]: 
                    
                    visited.append(i+1) # The element is add to the visited list.
                    
                    ready_queue.append(d_b[i+1]) # The burst time of the process in appended to the ready queue
                    
                    rq.append(i+1) # The corresponding process number is add to this list
                
            if process_number not in completed:  # If the process is not completed, it is again added to the ready queue.
                
                ready_queue.append(d_b[process_number]) # Adding the updated burst time of the particular process to the ready queue.
                
                rq.append(process_number) # Adding the process number.

            if not gantt or gantt[-1] != process_number: # if the previous process is also the same process that is being executed now, then there is not need of duplicates.

                gantt.append(process_number) # Adding the process to the gantt chart for displaying purposes.

        # Turn Around Time Computation
        for i in range(n):
            
            t_a_t[i] = d_c[i+1] - d_a[i+1]

        # Waiting Time Computation.  WT = TAT - BT
        for i in range(n):
            
            waiting_time[i] = t_a_t[i] - burst_time[i]
            
        Average_waiting_time = sum(waiting_time) / n

        Average_turnaround_time = sum(t_a_t) / n

        pass
    
 
    
    data = []
    
    for i in range(n):

        
        

        data.append([process_sno[i],arrival[i],burst_time[i],d_c[i+1],t_a_t[i],waiting_time[i]])


    print(data)

    print(gantt)
    res = {
        "data" : data,
        "Avg_t":Average_turnaround_time,
        "Avg_w":Average_waiting_time,
        "gantt":gantt
    }

    

    return render(request,'home.html',res)

    