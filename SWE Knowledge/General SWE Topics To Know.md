-ACID (database) - Atomicity, Consistency, Isolation, Durability
	-A transaction is a single logical unit of interaction on a database. In order to maintain database integrity these things must be maintained.
	-Atomicity - A transaction is treated as a single, indivisible unit of work, either all of it is completed successfully, or none of it. (No partial results).
	-Consistency - A transaction must leave the database in a consistent state, adhering to all defined rules, constraints, and relationships. (No breaking the rules).
	-Isolation - Transactions must execute independently of each other. Intermediate states of a transaction must not be visible to other transactions. (Privacy matters).
	-Durability - Once a transaction is committed, the changes are permanent, even in the case of a system crash. (Things actually stick after crash).

-Data padding - compilers often align data by padding non-word aligned types with empty bytes. This is for hardware efficiency. Accessing non word aligned data types can lead to tricky situations.

-On single thread single CPU machine OS cannot run while another program is running, OS is a program just like anything else.

-Binary search middle calculation: 
```python
mid = low + (high - low) // 2
```

-Prim's Algorithm to get minimum spanning tree:
	-Start somewhere, put all connection distances from there onto a min heap.
	-For each node, the minimum distance of it's connections is the minimum distance it takes to get to it from any other node
	-seen_nodes set allows us to only add the minimum connection for each node
	-Instead of "start here, and find smallest path to continue" we are more saying "start here, and what is the minimum path from anywhere to get to me"
	-Once seen_nodes is full (has each node in it) we know all points are connected
	-Time complexity: nested loops from 0->N = O(N^2), on each iteration we add element to heap = O(log(N)). technically is log(N^2) but this = 2log(N) and forget constants
	-Space complexity is the same, we add to heap each loop = O(N^2) but no extra space for the pushing operation
```python
class Solution:  
    def minCostConnectPoints(self, points: List[List[int]]) -> int:  
        # Time complexity: O(n^2 log(n))  
        # Space complexity: O(n^2)  
        n = len(points)  
  
        if n < 2:  
            return 0  
  
        min_heap = [(0, 0)] # distance, node connecting to  
        cost = 0  
        seen_nodes = set()  
  
        while len(seen_nodes) < n:  
            dist, i = heapq.heappop(min_heap)  
  
            if i in seen_nodes:  
                continue  
  
            seen_nodes.add(i)  
            cost += dist  
            x_i, y_i = points[i]  
  
            for j in range(n):  
                if j not in seen_nodes:  
                    x_j, y_j = points[j]  
                    nei_dist = abs(x_i - x_j) + abs(y_i - y_j)  
                    heapq.heappush(min_heap, (nei_dist, j))  
  
        return cost
```


Dijkstra's Shortest Path Algorithm:
	-Start at given node from parameter k with number of nodes being parameter n
	-Generate a graph as a defaultdict (python specific adjacency matrix)
	-Start heap off with having (0 (distance from source to itself), source)
	-For each connection in that the source has this will be the min time to reach that node
	-As we push and pop nodes in this order, they are organized by signal travel time from the node that pushed them
	-When we pop we are guaranteed that this is the minimum time it takes to get to this node
	-"Time and space complexity are too complicated to realistically be asked to explain"
```python
class Solution:  
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:  
        # Time complexity: O(V + E log(V))  
        # Space complexity: O(V + E)  
        graph = defaultdict(list)  
        for u, v, time in times:  
            graph[u].append((v, time))  
  
        min_times = {}  
        min_heap = [(0, k)] # distance from source to node, node  
  
        while min_heap:  
            time_k_to_i, i = heapq.heappop(min_heap)  
            if i in min_times:  
                continue  
  
            min_times[i] = time_k_to_i  
  
            for nei, nei_time in graph[i]:  
                if nei not in min_times:  
                    heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))  
  
        if len(min_times) == n:  
            return max(min_times.values())  
        else: return -1
```

Conditional variables - a synchronization primitive used in multithreaded applications to allow a thread to wait until a specific condition becomes true, essentially acting as a mechanism for threads to pause their execution and be notified when a certain state is reached by another thread.

-OSI (Open Systems Interconnection) Model
	-Layered from top (Layer 7) to bottom (Layer 1)
1) Physical layer - transmits raw bit stream over the physical medium
2) Data link layer - defines the format of the data on the network
3) Network layer - decides which physical path the data will take
4) Transport layer - transmits data using transmission protocols including TCP and UDP
5) Session layer - maintains connections and is responsible for controlling ports and sessions
6) Presentation layer - ensures the data is in a usable format and is where data encryption occurs
7) Application layer - human-computer interaction layer, where application can access the network services
	-User interface, protocols like HTTP, FTP

Heap vs. Stack:
-Stack - region of memory that stores data in a last in first out manner. 
	-Memory is allocated and deallocated automatically when functions are called and return
	-operations on the stack are extremely fast because the system always knows where the top of the stack is
	-the stack has a limited size, which can lead to stack overflow if too much memory is used
-Stored on stack:
	-Function call information: return addresses, function arguments (passed during the call)
	-Local variables
	-Control flow data - information to manage program execution
	
-Heap - a region of memory used for dynamic memory allocation. Unlike the stack the heap doesn't follow any strict order. Memory can be allocated and freed at any time, from anywhere in the program.
	-Manual memory management - in many languages you need to manually allocate memory, some have automatic garbage collection
	-Flexible size - the heap can grow and shrink as needed
	-Slower access - the heap memory is slower because the system has to search for free space and manage size
-Stored on heap:
	-Dynamically allocated objects - linked lists, trees, graphs that grow and shrink
	-Large data - that may exceed stack limits
	-Objects with long lifespan - aka data that persists beyond the scope of a function




RTOS:
	-RTOS guarantees deterministic timing, while general purpose OS focuses on maximizing throughput
	-RTOS has minimal overhead, while a general purpose OS manages many background tasks'



Watchdog timer - a hardware timer that resets the system if software fails to refresh it periodically
DMA - Direct Memory Access - allows peripherals to transfer data directly to and from memory without CPU intervention


C vs. C++:
	-C is a procedural programming language whereas C++ can be both procedural and object oriented
	-C++ includes things like classes, inheritance, polymorphism, and exception handling, which are absent in C.
	

