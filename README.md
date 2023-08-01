## Tic-Tac-Toe (DIP & OCP) & Minimax Algorithm

#### Using following Reference to create Open-Closed Principles (OCP) and Dependency Inversion Principles (DIP)
 ##### - https://docs.python.org/3/library/abc.html
 ##### - https://towardsdatascience.com/how-to-use-abstract-classes-in-python-d4d2ddc02e90


### Dependency Inversion Principles (DIP)
‘A dependency exists when a change in some element of software may cause changes in another element of software’ [1].
Reduce dependencies & make them explicit & identify each.
The program is dependent on abstract classes not on concrete classes.
High level modules not dependent on low level modules, additionally details only in low level modules depend on the abstraction.
Your dependencies point upwards (abstraction)


### Open-Closed Principle (OCP)
Classes open for extension but closed for modifiable.
‘hinge points in a design’ [1], OCD with LSP = DIP.
‘…we want to be able to change what the modules do, without changing the source code of the modules’ [2].


### Liskov Substitution Principle (LSP)
Related classes conforming to each other, if:
Sub-typing but no code extension (abstract class/ interfaces)
Code extension but no sub-typing (composition) polymorphism
Avoiding private variables/ operations in parent/ Super-Type class
Avoiding implementing new variables/ operations in child class/ Sub-Type
Over-ridden methods in child/ Sub-Type class accept the same input/ output values as parent/ Super-Type class.


### UML Design
![UML_tick_tac_toe](https://github.com/leakydishes/advanced_algorithms/assets/79079577/c6ea8b91-32cf-472c-a983-32ea1ea894ab)

## Reflection

### As seen in the last game play, if the user doesn't select 'smart' paths the bot appears to also not choose the 'smart' path. 
### However when player selects 'smart' paths the bot also selects. 
