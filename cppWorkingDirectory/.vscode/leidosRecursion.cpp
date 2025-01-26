#include <iostream>

unsigned long long factorial_recursive(int x);
unsigned long long factorial_iterative(int x);

int main() {
    for(int i = 0; i < 100; i++) {
        std::cout << i << "!: \t";

        std::cout << factorial_recursive(i) << " \t";

        std::cout << factorial_iterative(i) << " \t";

        std::cout << std::endl;
    }

    std::cout << "Press enter to close..." << std::endl;
    std::cin.get();
    return 0;
}

unsigned long long factorial_recursive(int x) {    
    if(x == 1 || x == 0) {
        return 1;
    } else {
        return (x * factorial_recursive(x - 1));
    }
}

unsigned long long factorial_iterative(int x) {
    unsigned long long ans = 1;
    for(int i = x; i > 0; i--) {
        ans = ans * i;
    }
    return ans;
}