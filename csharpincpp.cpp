// Example of how C# was created
#include <iostream>
#include <string>
using namespace std;


//Creates Class
class ConsoleCommand {
    public:
    // These are functions just like you would see in C#
    void WriteLine(string output) {
    cout << output;
    }
    void WriteLine(int output) {
    cout << output;    
    }
};

int main()
{
    //This line creates the Console object
ConsoleCommand Console;
/*
This line creates a string just like it would in the programming language C#.
Change it for a different output.
*/
Console.WriteLine("Hello");
 
}
