#include <list>
#include <unordered_map>

class LRUCache {
private:
    int capacity;
    std::list<std::pair<int, int>> cache; // doubly linked list to house cache elements, maintain the order, most frequently accessed first
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> map; // unordered map is C++ dictionary

    void moveToFront(int key) {
        auto it = map[key]; // creates an iterator pointing to the element we want to move
        cache.splice(cache.begin(), cache, it); // splice is built in std::list method that moves elements from one part of the list to another
        // cache.begin() is iterator pointing front of the list, moving object at iterator it from data structure cache to that location
        // cache.end() would return iterator pointing directly after last elemtn in the list
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (map.find(key) == map.end()) { // just like cache.end, this returns just after final element, where iterator would end up if looking and not finding
            return -1;
        }
        moveToFront(key);
        return map[key]->second;
    }
    
    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            map[key]->second = value;
            moveToFront(key);
        } else {
            if (cache.size() == capacity) {
                int lrukey = cache.back().first; // cache.back() returns reference to the final element in the arrat, different than .end()
                // .first accesses the first element in the key value pair, ie. the key
                cache.pop_back(); // removes the last element in the list
                map.erase(lrukey); // after removing the item from the cache, this removes the key from the map
            }
            cache.push_front({key, value});
            map[key] = cache.begin();
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */