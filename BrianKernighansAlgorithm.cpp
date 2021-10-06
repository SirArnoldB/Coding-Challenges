#include <iostream>
#include <bitset>
using namespace std; 

// Function to count the total number of set bits in `n`
int countSetBits(int n) {
    // `count` stores the total bits set in `n`
    int count = 0;

    while (n) {
        // clear the least significant bit set
        n = n & (n - 1);
        //  count the least significant bit 
        count++;
        }

    return count;
    
    }

int main() {
    int n;
    cout << "ENTER THE VALUE OF N: \n"; 
    cin >> n; 

    cout << n << " in binary is " << bitset<32>(n) << endl;
    cout << "The total number of set bits in " << n << " is " << countSetBits(n) << endl;

    return 0;
}



