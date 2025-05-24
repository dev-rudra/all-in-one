#C++
### What is OOP in C++?
OOP (Object Oriented Programming) is a way of writing code where we think of real-world objects
(like cars, animals, or bank accounts) and represents them in code using classes and objects.

### In C++, OOP is based on 4 main ideas:
#### Class
* A blueprint for creating objects.
* It defines what data (variable) and actions (functions) an object will have.

```cpp
class Car {
public:
    string brand;
    
    void start() {
        cout << "Car started\n";
    }
};

#### Object
* An actual thing created from a class.

```cpp
Car myCar; // myCar is an object of the Car class
```

#### Encapsulation
Hiding the internal details and controlling access to data using access modifiers:

* Private: Only the class itself (Fully hides data from outside - most secure).
* Protected: The class + child (derived) classes (Hides data from outise, but allows access in child classes).
* Public: Not for hiding (Everyone). It exposes data/methods - but still used in encapsulation to offer controlled access (like get() and set()).

```cpp
#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance; // Hidden from outside

public:
    // Constructure
    BankAccount(double initialBalance) {
        if (initialBalance >= 0)
            balance = initialBalance;
        else
            balance = 0;
    }
    
    // public method to add money
    void deposit(double amout) {
        if (amout > 0) {
            blance += amout;
        }
    }

    // public method to get balance
    double getBalance() {
        return balance;
    }
};

int main() {
    BankAccount myAccount(1000.0);  // create an account with 1000
    myaccount.deposit(50.0);        // Deposit 50
    cout << "Balance: " << myAccount.getBalance() << endl; // show balance
}

/*
1. Private: Balance is hidden from outside.
2. Public: Safe ways to interact with balance.
3. deposit(): Allows adding money if the amount is valid.
4. getBalance(): Allows reading the balance safely.
*/
```
> [!TIP]
> You can't access balance directly like this `myAccount.balance = -500; // Not allowed - it's private`

### Example using protected

```cpp
#include <iostream>
using namespace std;

class Animal {
protected:
    string sound; // can be accessed by child class

public:
    void makeSound() {
        cout << "Animal sound: " << sound << endl;
    }
};

// child class

class Dog: public Animal {
public:
    void setSound() {
        sound = "Woof!"; // Allowed because 'sound' is protected
    }
};

int main() {
    Dog myDog;
    myDog.setSound();
    myDog.makeSound();

    myDog.sound = "Woof!"; // Not allowed 'sound' is protected
}

// sound is protected in the Animal class.
// Dog, which inherits from Animal, is allowed to access sound.
// Code outside the class (like main()) cannot access sound directly.
```
> [!NOTE]
> When you want child classes to have access to variables or functions.
> But you still want to prevent outside code from accessing them directly.


##### Why is Encapsulation Important?
* Protects data (eg, no direct access to change balance)
* Controls how data is changed or read
* Make code eaiser to maintain and debug

#### Inheritance
* A class can reuse another class's features.
* Example: A `Truck` can inherit from `Car`.

```cpp
class Truck public Car {
    // Inherits brand and start() from Car
};
```

#### Polymorphism - (One name many forms)
* One function can act differently depending on the object calling it.
* Useful when different classes share the same function name but behave differently.

##### Types of Polymorphism:
1. Compile-time polymorphism: (function overloading)
2. Runtime polymorphishm: (using inheritance and `virtual` functions)

We'll focus on runtime polymorphism, which is more commonly used in OOP.

Example:
```cpp
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void makeSound() {
        cout << "Animal makes a sound\n";
    }
};

// Derived class Dog
class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Dog says Woof!\n";
    }
};

// Derived class Cat
class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Cat says Meow!\n";
    }
};

int main() {
    Animal* a; // Base class pointer

    Dog d;
    Cat c;

    a = &d;
    a->makeSound(); // Output: Dog says Woof!

    a = &c;
    a->makeSound(); // Output: Cat says Meow!
}
```
