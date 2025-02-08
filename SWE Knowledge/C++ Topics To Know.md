```c++
std::unique_ptr<int> ptr1 = std::make_unique<int>(10);
std::unique_ptr<int> ptr2 = std::move(ptr1);
// no need to delete, ptr2 will automatically free memory when it goes out of scope

std::shared_ptr<Node> ptr1 = std::make_shared<Node>(20);
std::shared_ptr<Node> ptr2 = ptr1;  // Both ptr1 and ptr2 share ownership
ptr1.reset();  // Decrease reference count by 1
//Node will be destroyed when the last shared_ptr goes out of scope

std::shared_ptr<Node> sharedPtr = std::make_shared<Node>(30);
std::weak_ptr<Node> weakPtr = sharedPtr;  // Non-owning reference
if (auto temp = weakPtr.lock()) {  // Temporarily promotes to shared_ptr
    std::cout << "Value via weak_ptr: " << temp->value << "\n";
}
sharedPtr.reset();  // Destroys the Node as no strong references re

class FileHandler {
    ofstream file;
public:
    FileHandler(const string& filename) {
        file.open(filename);
        cout << "File opened.\n";
    }

    ~FileHandler() {
        if (file.is_open()) {
            file.close();
            cout << "File closed.\n";
        }
    }
};
```



-Storage duration: dynamic, thread_local, static, automatic
	-Dynamic - You must create and destroy! Special operator such as new can do this. This object will exist until corresponding delete operator is called.
	-Automatic - created upon entry to the code block enclosing the object, destroyed on exiting said code block. Local objects that are declared without static, extern, or thread_local specifiers.
	-Static - storage is created when the program begins execution and deallocated when the program ends execution. Storage created before the first reference to the object. (All namespace scope objects plus things with static or extern identifiers).
	-thread_local - similar to static but allocated when thread is initialized and deallocated when thread ends. Object is created before the first access to the object. Must be declared with thread_local identifier. Can also have extern or static identifiers, these do not effect storage duration and instead linkage.

-Access Control 
	-Determines how and where members of a class can be accessed outside of a class.
	-Major types: private, public, protected
		-Public - Members declared public can be accessed anywhere in the program, including outside the class. Methods or attributes that should be freely accessible.
		-Private - Members declared private can only be accessed within the class. (Not even accessible in derived classes). Useful for encapsulation, protecting sensitive data. (Can have a public method that modifies a private member).
		-Protected - Members declared protected can be accessed within the class and by derived classes. Not directly accessible from outside the class,. Useful for allowing derived classes to manipulate base class members while still restricting external access.

-Class Inheritance
	-Can be public, private, or protected. (Private is default if no access_specifier is provided)
	-Public inheritance - Both public and protected members remain as such in derived class.
	-Protected inheritance - Both public and protected members become protected in derived class.
	-Private inheritance - Both public and protected members become private in derived class.

-Strict Aliasing: when two pointers of different types are passed to a function, compiler automatically assumes they are non-overlapping, can cause non expected results. Also a pointer of a differing type than the data that is stored at a memory address cannot be assigned to that memory address. Also creates unpredictable behavior. (This is different in other programming languages, i.e.. Fortran).

-Size of a class - The size of a class is between 1 (The minimum) and the sum of it's data members. Data members can be thought of solely as declared or inherited variables. Methods are not data members. 
	-Size cannot be 0 as that would allow multiple objects to share the same memory address in one instance.

-Mutable - can be modified even by a method labeled const. 

```c++
class Example {
private:
	int value;

// This method is constant; it can't modify data members
	void privateConstMethod() const {
	// value = 10;  // Error: Cannot modify a non-mutable member
					// Adding mutable would allow this
	}

	// This method is NOT constant; it can modify data members
	void privateNonConstMethod() {
	    value = 10;  // Allowed
	}

public:
    void publicMethod() const {
	    // This is a public constant method
    }
};
```


-Classes vs. structs
	-Only major difference is everything defined in a class is private by default and everything defined in a struct is public by default
	-Classes are used for more complex situation while structs are typically kept more simple

-"&" in C++
	-As a reference operator - creates a reference to an already existing variable, forgoes copying, allows access to change original data

As a reference operator:
```c++
void updateValue(int& value) {
    value = 42; // Modify the original variable
}

int main() {
    int x = 10;
    updateValue(x); // Pass by reference
    std::cout << x << std::endl; // Output: 42
}		
```

Return by reference:
```c++
int& getElement(int arr[], int index) {
    return arr[index]; // Return a reference to the element
}

int main() {
    int numbers[3] = {1, 2, 3};
    getElement(numbers, 1) = 42; // Modify the second element directly
    std::cout << numbers[1] << std::endl; // Output: 42
}
```
Without the `&`, the function would return a copy of the element, and modifications would not affect the original array.

Straight up variable declaration:
```c++
int a = 10;
int& ref = a; // ref is now an alias for a
ref = 20;     // Modifies a directly
std::cout << a << std::endl; // Output: 20
```

-Pointers vs. Iterators:
	-Pointer is simply a memory address that points directly to a variable or data in memory
	-Iterator - an abstract object that behaves like a pointer but is designed to work with containers (vector, list, map, etc.)
	-Iterator provides a standard way to traverse elements without worrying about underlying memory layout

```c++
vector<int> v = {1, 2, 3};
vector<int>::iterator it = v.begin(); // iterator to the first element
```

***Pointers and References are somewhat inverse of each other, pointer holds mem address, reference holds alias of the value, behaves like the original variable without the need for dereferencing

| Aspect              | Pointer                                               | Iterator                                                                        |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------- |
| Data Structure      | Works with raw arrays or dynamically allocated memory | Works with STL (standard template library) containers (vector, list, map, etc.) |
| Abstraction         | Low-level (direct memory access)                      | High-level (abstract data structure details)                                    |
| Flexibility         | Limited to simple data structues                      | Can travers complex data structure                                              |
| Safety              | No bounds checking (prone to segmentation faults*)    | Safer, often with built-in checks                                               |
| Customization       | Cannot be customized                                  | Can be customized via operator overloading                                      |
| Container Awareness | Unaware of the data structure                         | Aware of container-specific properties (like begin() and end())                 |
*Segmentation faults - program tries to access memory it doesn't have permission to access.

Multithreaded locking and unlocking:
-wait()
```c++
	void wait(std::unique_lock<std::mutex>& lock, Predicate pred);
```
lock -> A lock that must be acquired before calling wait()
pred -> A lambda function (or callable) that returns true when the condition is met
	-If pred is false, thread sleeps
	-If pred is true, wait() returns immediately
-When wait is called:
	1) Automatically unlocks mutex (lock.unlock()) allowing other threads to access shared resources
	2) Puts the calling thread to sleep until another thread calls notify_one() or notify_all()
	3) When notified it re-acquires the mutex (lock.lock()) and check the condition pred.
		-If pred is true, execution continues
		-If pred is false, the thread goes back to sleep

-notify_one()
```c++
my_conditional_variable.notify_one();
```
-When the consumer consumes an item, it calls notify_one()
-This wakes up the producer waiting in wait(), allowing it to produce a new item

-notify_all()
```c++
my_condtional_variable.notify_all()
```
-Wakes all waiting threads, allowing multiple processes to proceed

-Functions must be declared before they are called or defined before their usage

-std::list: begin() and end() both return iterators to the first element in the list and the position directly after the final element in the list.

-'this' keyword is a pointer that refers to the current object of the class in C++, when inside a constructor or method within a class, 'this' gives access to the object's own members (like variables and methods).
-To dereference this pointer, we can use '->' these two are equivalent:
```c++
LRUCache(int capacity) {
	this->capacity = capacity;
}

LRUCache(int capacity) {
	(*this).capacity = capacity;
}
```
- '->' is a member access operator, similar to obj.data or &a 
- ONLY WORKS WITH POINTERS
- It is essentially a combination of dereferencing (*) and Accessing (.)

-File Access:
	-fstream is library for file access, provides three main classes:
		-std::ifstream - for reading files
		- std::ofstream - for writing to files
		- std::fstream - for reading and writing to files
	-These use .open() and .close()

```c++
#include <fstream>
#include <iostream>
#include <string>

int main() {
	std::ifstream inputFile("exmaple.txt"); // opens file for reading
	if (!inputFile) {
		std::cerr << "Failed to open file." << std::endl;
		return 1;
	}
	
	std::string line;
	while (std::getLine(inputFile, line)) {
		std::cout << line << std::endl;
	}
	inputFile.close();

	std::ofstream outputFile("otherEcample.txt");
	if (!outputFile) {
		std::cerr << "Failed to open second file." << std::endl;
		return 1;
	}
	outputFile << "Hello, World!" << std::endl;
	outputFile.close()

	return 0 ;
}
```


Linked Lists / pointer basics:
```c++
struct ListNode {
    int val; // data part of the node, holds the actual data stored within the node
    ListNode *next; // this is a pointer to the next node in the linked list

    // constructors - special functions used to initialize objects when they are created

    ListNode() : val(0), next(nullptr) {} // default constructor, when creating a node with no value
    //ex: ListNode node;

    // parameterized constructors
    ListNode(int x) : val(x), next(nullptr) {} // initializes value to x and next to nullptr
    //ex: ListNode node(5)
    ListNode(int x, ListNode *next) : val(x), next(next) {} // initializes value to x and next to point to next
    //ex: ListNode node(5, &nodeName)
};

int main() {
    //some example usage!
    ListNode node1(1); // make three nodes
    ListNode node2(2);
    ListNode node3(3);

    node1.next = &node2; // 1 -> 2 -> 3
    node2.next = &node3;

    // creates a pointer of type ListNode that points to the memory address of node1
    ListNode* current = &node1;
    while (current != nullptr) {
        std::cout << current->val << " -> ";
        current = current->next; // memory access operator, used to access elements of pointers
        // current is a pointer so we need to dereference and access its elements
    }
    std::cout << "nullptr" << std::endl;
    return 0;
}
```

Dynamic memory allocation - allows you to allocate memory at runtime (instead of compile time). This is useful when you don't know the size of data in advance. ex: linked lists, dynamic arrays, trees.

-Heap vs. Stack memory:
	-Stack - automatically managed memory ie. local variables
	-Heap - manually managed memory ie. using new/delete in cpp

```c++
ListNode* node = new ListNode(42);
//do something with node
delete node;
```
-In this example without delete, you would have a "memory leak" which means that memory fails to be released when it is no longer needed, leading to locked memory and wasted resources. Leads to increasing amounts of worthless memory.

Modern C++ has SMART POINTERS!
-These are part of C++ 11 standard and help to prevent memory leaks and dangling pointers - pointers that hold memory addresses of things that have been destroyed

-C++ provides three kinds of smart pointers, all defined in the <memory> header
	1. std::unique_ptr - exclusive ownership
	2. std::shared_pointer - shared ownership with reference counting
	3. std::weak_ptr - non-owning reference to prevent cyclic references

1. unique_ptr - owns a resource exclusively, only one unique_ptr can manage a given object at a time
	-When one of these goes out of scope it automatically deletes the managed object
	-Cannot be copied but can be moved using std::move

2. shared_ptr - allows multiple pointers to share ownership of the same resource
	-Internally uses reference counting, each new shared_ptr increases the count, and when the count drops to 0, the resource is freed
	-Useful for graphs, trees, or shared resources

3. weak_ptr - a non-owning smart pointer that references an object managed by shared_ptr
	-does not affect the reference count
	-can use .lock() to convert a weak_ptr to a shared_ptr temporaroly
	-Used to prevent cyclical references, common in graphs


-Moving objects - in cpp moving means to transfer the ownership of resources from one object to another. Is efficient with no resource duplication

vector<int> vec1 = {1, 2, 3, 4, 5}; 
vector<int> vec2 = move(vec1); // Move constructor is called

Can be copied:
	-Primitive types (int, double, char)
	-Standard containers (string, vector)

Cannot be copied:
	-unique_ptr
	-mutex

Can be moved:
	-unique_ptr
	-standard containers

Cannot be moved:
	-mutex
	-objects with deleted move constructors

Destructor: the opposite of contructors.
	-Name of class with a  '~' prefix
	-Never any parameters or return type

Destructors are required whenever:
	-you are managing dynamic memory (new/delete) - you must free the dynamic memory in the destructor to prevent memory leaks. Also whenever
	-Releasing non-memory resources - using files, sockets, or database connections


In C++ nullptr is a type safe null pointer, instead of being null (which is just 0) null ptr has it's own type std::nullptr_t preventing ambiguities in function overloads

Destructors are only necessary when doing Dynamic Memory handling

Shallow copy - only copies the memory address of the object, if original data is modified so is this copied version (it's the same data)
Deep copy - Actual copy of the data itself is created


Virtual functions and polymorphism - Virtual functions enable runtime polymorphism (dynamic dispatch) in C++ - they allow functions to override base class behavior keyword virtual goes before return type

Virtual inheritance actually different this avoids diamond problem and 


Abstract class - a class with at least one pure virtual function (=0) meaning that it cannot be instantiated
	-Used as a base class for defining an interface

