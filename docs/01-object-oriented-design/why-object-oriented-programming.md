# Why Object Oriented Programming ?

## Introduction:
Before modern object oriented programming languages became mainstream, most business software was written using procedural programming.

Let say we have to develop a Bank Management System. How do you build the software ?

## Bank Example
### Business Requirements
A simple bank system that should store user's account balance safely. User will create account on that Bank. Account holder will deposit money and withdraw money from the Bank. User also check account balance.

### Implementation
- I'll create a function that will take account ID and account holder name as input. Then persist account information into a global storage using account ID. Initial balance is zero.
- Another function to deposit money into the Bank account. User will provide account ID and amount as input. The function should increase account balance using input amount.
- A money withdrawal function take account ID and amount as input. Should reduce account balance with input amount.
- A function will take account ID as input. Fetch account and return/print balance from the account.

Super easy. Simple program including a data storage, four procedure to operate the Bank system. 

### Business Grows
Now let's provide some validation on our Bank system. 
- Without owner name a Bank account can't create.
- Negative amount shouldn't deposit.
- User will be allowed to withdraw maximum amount upto remainig balance.
- If wrong account ID provided then notify given informations are invalid.

After implement these validation rules the system working fine. User's is now restricted to negative deposit or notified when try to withdraw insufficient amount.

But our Bank system still missing many features that other system is providing.

Let's add some more.
- VIP account creation.
- Fund transfer.
- Credit card management.
- Loan management.
- Early settlement.
- Account ledger management.
- Audit logs.
- SMS notifications.
- Auto email notification.

The system is now much more feature-rich than before. User's have so many options in our Bank system. Our program has quickly grown from 200 lines to over 1,500 lines of code.

But wait... did you notice something ?

The problem is each procedure/component of the program can access, modify the account balances from anywhere of the program. **Application data is exposed.**

Is it safe ? 

Unfortunately, no. Current problems:
- Currently anyone can modify any accounts information from the storage since there is no data integrity itself. 
- Any part of the program can override the money deposit rules and deposit negative amount. Even one can delete a account without any restriction.
- There is high chance to bypass business rules. No one is forcing to follow business rules.
- Think about newcomer of the team. Is it easy to adoption ? Juniors can understand it easily ? Maybe not.
- When there will raise an issue, it's too hard findout the root cause immidiately since developer have to read full code base to trace the issue. Because business rules are scattered through the whole program.

### Real world example
A Bank vault could be a real analogy.

Bank vault stores customer's balance. Imagine anyone of the Bank stuffs has access to the vault instead of a single authorised person(Vautl officer). Even Bank receptionist can modify the vault balance wihtout following any rules.

### Maintaining the System
For example balance mismatch issue raised. But developer doesn't know the origination point from where balances updated. Developer now reading the whole code base.

But how nice it could be if the balance update rules, business logic had kept somewhere related to the account itself ? 

Any component of the program will go through that place to modify account balance. If so, developer's will read only that business rules and can easily findout the root cause of balance issue. Am I right ?

For each of problem discussed above, could follow these convention and practises. Money deposit or withdrawal business will keep in such place where they should be. **Business rules should live with the entity that owns the data**. If it is, then each part will give safe guard of own data using own rules. Any issue raised, go through the responsible area to find and resolve the issue easily.

Now notice another thing, following above convetion our code base becoming maintainable. We can also add new features easily but still code will organize and traceable. Growing business rules system should work perfectly as like before. Since our data will update through responsible area there is another layer added that protecting our data from being modified easily now. How amusing it now :)

## Object-Oriented Thinking
The solution is to organize software arround objects (or responsible entities) that own both their data and the bahaviors that ensure validity of that data.

## Key Takeaways
- **Procedural programming can solve business problems, but software becomes harder to maintain as complexity grows.**
- **Business rules become scattered when data and behavior are separated.**
- **Exposed data increases the risk of bypassing important business rules.**
- **Object-oriented design organizes software around responsible entities that own both their data and the behaviors that protect it.**

