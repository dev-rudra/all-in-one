// standard input-output stream library.
#include <iostream>
#include "bankAccount.h"

using std::string;

class Employee {
public:
    string Name;
    string Company;
    int Age;
    
    void IntroduceYourself() {
        std::cout << "Name: " << Name << std::endl;
        std::cout << "Company: " << Company << std::endl;
        std::cout << "Age: " << Age << std::endl;
    }
};

int main() {
    // BankAccount
    BankAccount myAccount(100.0);
    myAccount.deposit(50);
    std::cout << "Current Balance: " << myAccount.getBalance() << std::endl;
    std::cout << std::endl;
    
    Employee emp1;
    emp1.Name = "Rudra";
    emp1.Company = "Japannext";
    emp1.Age = 29;
    emp1.IntroduceYourself();
}
