//
//  bankAccount.h
//  CPP
//
//  Created by Rudra on 2025/05/24.
//
#ifndef BANKACCOUNT_H
#define BANKACCOUNT_H

class BankAccount {
private:
    double balance;

public:
    // constructure
    BankAccount(double initialBalance) {
        if (initialBalance >= 0)
            balance = initialBalance;
        else
            balance = 0;
    }
    
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
    
    double getBalance() {
        return balance;
    }
};

#endif
