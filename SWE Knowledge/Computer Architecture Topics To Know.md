
Cache Thrashing - occurs when multiple memory locations that are frequently accessed map to the same cache line, causing constant evictions and reloads from the main memory. Significantly reduces CPU performance because the cache is not being utilized efficiently.

This can occur due to:

-Poor memory access patterns - if multiple threads frequently access memory locations that conflict in the cache each access forces an eviction of previously stored data

-Associativity limitations - caches have a limited number of ways (sets) to store data. If too many memory addresses map to the same set, the CPU has no choice but to keep evicting and reloading data.

-Multi-threading conflicts - multiple threads accessing adjacent memory addresses on different cores may cause cache invalidations. Since modern CPU's use cache coherency protocols, one core's modifications to a shared cache line forces reloads on other cores.

  
How to prevent cache thrashing:

-Improve data locality - Access data in sequential order rather than in a scattered pattern. Use row-major order for arrays.

-Row-major order: storing matrix elements row by row instead of column by column (default for C, C++, Python)

-Increase cache associativity - Some modern CPU's allow adjusting cache associativity to reduce conflicts.

-Use padding to prevent false sharing - add extra bytes to separate frequently accessed data into different cache sets.

-Prefetch data - use compiler optimizations like loop unrolling or manual prefetching.

-Optimize multi-threading - use thread-local storage or NUMA-aware memory allocation to prevent threads from stepping on each other's cache lines.

  

Cacheing Process:

1. CPU core accesses a memory location that is not in it's cache, it fetches a cache line (usually 64 bytes) from RAM into its cache.

2. If CPU modifies that data the cache line becomes "dirty" which means that it has been modified but not yet written to RAM. Which is done by modification of it's state bits.

3. Modern CPUs follow MESI (Modified, Exclusive, Shared, Invalid) or a similar protocol to track state of cache lines:

      -Modified - The cache line has been modified by this core and differs from data in RAM.

      -Exclusive - The cache line is unmodified and only exists in this core's cache.

      -Shared - The cache line is identical to what is in RAM and may exist in other cores.

      -Invalid - The cache line is no longer valid (another core updated it).

      If another core requests the same memory, the current core must respond with the updated data before allowing access.

  

4. Write-Backs vs. Write-Through:

      -Write-Back - Most common in modern CPU, the modified cache line stays in the cache and is written back to RAM only when      evicted or when another core needs it.

      -Write-Through - Less common but used in embedded systems, every write immediately updates RAM, ensuring RAM always has       the latest data. This simplifies cache coherence but is slower.

5. Eviction and write back to RAM - when a CPU cache runs out of space, it may evict a "dirty" cache line, forcing it to be written to the RAM. This is managed by the cache replacement policy (LRU - Least Recently Used) or (LFU - Least Frequently Used).

6. Disk policy - The CPU DOES NOT write directly to the disk. Writes to the disk only happen when the operating system flushes data from RAM to storage, usually through system calls like fsync() or periodically by the OS.

  

  

Cache coherence protocol helps cores keep track of what other cores have in their cache. There are two primary methods used to maintain coherence across multiple cores:

  

1. Bus Snooping (Used in small to medium core systems (up to 16 cores)) - cores use a shared bus to monitor each other's memory accesses.

a. Every core's cache listens (snoops) to memory transactions from other cores.

b. whe one core requests a memory address, the other cores check their own caches.

c. If another core has a modified version of that data, it must respond with the latest copy.

d. this prevents an old version in RAM from being used when a newer version is in a cache.

  

Example:

      1. Core 0 loads memory address x from RAM, marks it as (E) Exclusive state.

      2. Core 0 modifies x, transitioning the cache line to (M) Modified/Dirty.

      3. Core 1 requests x:

            i. Instead of reading from RAM, Core 0 sends the latest modified value directly to core 1.

            ii. Core 0 either: marks x as (S) Shared (if read) or invalidates its copy if Core 1 writes to x (forcing core 1        to take ownership 

      -RAM never sees the intermediate change - only the final written-back value when needed.

      -As number of cores increases, bus contention becomes a bottleneck.

  

Throughout this process, if no core responds to a request for memory in a certain arbitration cycle, the cache controller assumes it is only in RAM. Each core has it's own cache controller. The cache controller is what checks the directory in RAM (or a dedicated cache directory). Cache controllers communicate through a coherent interconnect such as Intel's Mesh Interconnect or AMD's Infinity Fabric.

  

2. Directory-Based Coherency (used in large multicore systems) - maintained directory reflects core cache data storage.

  

a. The system maintains a directory in RAM (or a special cache) that tracks which cores have copies of a given cache line.

b. Each block RAM has associated metadata: which cores have a copy? Is the data clean (matches RAM) or dirty (modified in cache)? c. When a core needs data, it consults the directory instead of broadcasting results to all cores.

  

Example:

      1. Core 0 loads memory address x into it's cache. The directory in RAM records "x in core 0 (state: Exclusive)".

      2. Core 0 modifies x. The directory updates "x is in core 0 (state: Modified)".

      3. Core 1 requests x. Instead of reading from RAM, the directory sees that core 0 has a modified copy.

      4. The system forwards the request to core 0.

      5. Core 0 sends the latest data to core 1.

      6. The directory updates to reflect core 1 now having the latest data.

  

Cache controllers in modern CPU:

   -L1 Cache Controller - each core has a private L1 cache (instruction + data) with it's own L1 cache controller.

   -L2 Cache Controller - Some CPUs have private L2 caches per core, while others share L2 across a few cores.

   -L3 Cache Controller - Most CPU's share an L3 cache across all cores, this handles requests from all cores and    communicates with the memory controller.

  

Memory controller (External to cores, handles RAM access) - sits between the L3 cache and DRAM, handles data requests that miss all cache levels.

  

  

Conflict vs. Capacity Miss:

  

Conflict:

- Can occur in direct-mapped or set associative cache, not fully associative caches.

- When multiple RAM lines map to the same cache line and cache must evict one to use the other.

  

Capacity:

- Happens in all kinds of caching.

- When a  program's working set (active memory footprint) is larger than the cache size, forcing the cache to evict data that will soon be needed. Basically when a cache is not big enough for a given program.

  

  

Cache line size, file sharing, and padding - When two threads modify two different variables in the same cache line, performance suffers due to coherency traffic. This makes padding a very good idea - which is separating frequently modified variables across different cache lines by adding extra unused bytes to fully populate one row.

  

Cache prefetching - modern CPU's use hardware prefetchers that predict future memory accesses and load data into cache before it's needed. Two kinds are:

      -Spatial prefetching - loads nearby cache lines, e.g. if iterating through an array prefetcher can pull next few cache              lines in anticipation of iterating the whole array

      -Temporal prefetching - anticipates data that will be used again soon and keeps it in the cache, e.g. incrementing the              same value multiple times through a loop, can keep that variable in the cache, it will be needed each iteration

      -This can be very nice for linked lists, which use non contiguous memory addresses, always prefetching the .next node

      -hardware prefetcher is built into the CPU and monitors memory access patterns at runtime and speculatively preloads data           into the cache before it is explicitly requested. This can reduce access latency by hiding the delay of fetching. 

  

Translation Lookaside Buffer (TLB) - a cache for virtual-to-physical memory translations

      -Reduces memory translation overhead

      -Has L1 and L2 TLBs, just like regular caches

      -Uses page table entries (PTEs) for address lookups

  

Types of caches:

   -Victim cache - small buffer containing recently evicted cache lines from L1
   -Inclusive cache - L3 contains everything in L2 and L1, making data easier to find
   -Exclusive cache - L3 contains data not present in L2 or L1, maximizing cache space


Cache line locking - certain performance-critical operations (e.g. real-time applications) can lock cache lines to prevent eviction


Locking a thread to a specific core to prevent it from being scheduled on different cores (reducing context switching and improving cache locality), you can use CPU affinity.

-This ensures:

1. The thread always runs on the same CPU core.

2. Reduces cache misses due to unnecessary CPU migrations.

3. Helps with real-time performance.

-Probably not a thing to learn how to do but knowing that you can do that in both Linux and Windows