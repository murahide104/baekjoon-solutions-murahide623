#include <iostream>
#include <ctime>
using namespace std;

int main() {
    time_t now = time(0);
    tm* timeinfo = localtime(&now);
    
    char buffer[80];
    strftime(buffer, 80, "%Y-%m-%d", timeinfo);
    cout << buffer << endl;
    return 0;
}