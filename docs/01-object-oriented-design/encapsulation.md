# Encapsulation
At the end of the previous lesson, we indentified several limitations of procedural programming. If we notice the key takeaways of previous lesson we can see there were some problems like:
- Maintainability issue.
- Debugging complexity.
- Business rules are scattered, so there is a chance to bypass business rule.
- Application data has exposed.

To address these issues we arrived at object-oriented thinking.

## What Problem Does Encapsulation Solve?
In the BankAccount example 
- we have seen that almost every procedure, components are access accounts storage from anywhere of the program and that exposed applciation data. The data can't protect itself. Even anyone can delete an account from the storage.
- If any issue raise related to balance update then developers have to read the whole program. Because balance update logic scattered through the whole program.
- Anyone can deposit negative amount or try withdraw money bypassing maximum amount validation.

Cosider the real world analogy of a bank vault where every staff member has access to it. That would be extremely risky. But how would be if there is a vault officer who is responsible for the vault. Anyone come for money withdraw, provide money withdrawal request, vault officer check identity & account authorization, post transaction, update ledger and finally release cash from the vault. 

The benefit of having the vault officer is not about vault security. It's about responsibilities & related operations executed by the vault officer. If anyone will allowed to withdraw cash from the vault then they may won't execute all the operations like vault officer. If so all related records would be stale. So, here only the vault officer should have withdrawal access instead of all staff.

Now come to the technical point. The Bank Account balance should be update through a responsible process that will ensure validity of the balance and related actions/transactions has been executed. Instead of update balance from anywhere of the program if developer use a well organized method to update balance it would be better. Inside that method all the validations and business rules will be applied. Then anyone won't update balance directly, no more chance to bypass business rules, no more chance to negative balance deposit or maximum withdraw rules violation. 
The balance-changing method becomes a clear entry point for investigating any balance related issues, rather than having arbitrary code modify the balance from different places.

From this discussion we can tell that the balance and related processes, rules, validations should live together. And this is the essence of encapsulation.

## Why Exposing Business State Is Dangerous
In the BankAccount example if we update balance directly then anyone can't tell the reason of balance update. Any related transactions won't be executed. The method doesn't check amount is negative or something else. One can update wrong value mistakenly.

Here BankAccount balance is business state. So to allow anyone update balance directly means expose business state and it's too dangerous. This will create business inconsistency and related records will be stale.

## Behavior-Oriented vs State-Oriented Design
Balance is a state of the BankAccount entity. Whereas negative amount deposit rules and maximum withdrawal rules are behaviors of the entity. Imagine there are methods called 
- udpate_balance(account_id, amount)
- deposit(account_id, amount)
- withdraw(account_id, amount)

The update_balance method takes amount and update balance directly. This method do nothing else inside instead of balance update. The name of the method doesn't provide hint about balance update reason. Even developer's can't imagine was it deposit or withdraw of money.

On the other hand deposit, withdraw methods name is self explanatory. Anyone can understand that the method should do something like money deposit or withdraw from the account. And there may contains negative amount deposit validation, maximum amount withdraw validation.

This the difference and advantages between behavior-oriented and state-oriented design. The update_balance method is allowing user to update state directly and no-one is forcing to follow business rules, the method knows nothing about the business reason behind the state change.

## Why Getters and Setters Are Not Enough
A getter and setter can provide an API boundary, but a simple setter doesn't neccessarily provide meaningful encapsulation. Getters and Setters do not necessarily prevent direct state changes. Encaptulation is not about make restriction to change state or make developers life harder. It's about making the way of state changing easy, following business rules and forcing developer's to follow and maintain business rules when changing business state.

As example update account balance directly or update using a setter method called set_balance(self, amount) has no difference. The actual benefit occurs when the method forces to follow relevant business rules instead of changing the state directly. 

## The Architectural Meaning of Encapsulation
Encaptulation means keeping business state together with the behaviors responsible for protecting and chaning that state. Instead of exposing APIs that directly manipulate business state, expose behavioral APIs that represent meaningful business operations. The behavioral API will force to follow business rules on behalf of change the business state.

Getters, setters, private members, and protected members are language features that can help establish encapsulation, but they are not the essence of encapsulation.

## Key Takeaways
- **Encapsulation concept allow to keep together business state and behaviors that protect the state.**
- **Encapsulation is not make restriction of state change or make developers life harder. It's about force to follow business rules in a easy way and keep business consistent.**
- **Encapsulation is not about setter, getter, private or protected these are just language features. Encapsulation emphasizes that business state should be changed through the responsible behavior rather than arbitrary direct modification.**