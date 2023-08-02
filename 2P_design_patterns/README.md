# Tic-Tac-Toe (DIP & OCP) & Minimax Algorithm
### Open-Closed Principles (OCP) and Dependency Inversion Principles (DIP)

‘…what is a good written piece of code and what is not'


Good Design
-	OOP principles followed
-	Good Design Principles
o	Dependency Inversion Principle
o	Open/ Closed Principle
o	Responsible use of Inheritance

### Design Patterns
o	Factory Patterns
o	Observer
o	Iterator

###	Test Cases
o	Consider standard input ‘hack it through a standard input’ [1]
o	Where are the cases where the functionality will fail?


##Dependency Inversion Principles (DIP)
‘A dependency exists when a change in some element of software may cause changes in another element of software’ [1].
- Reduce dependencies & make them explicit & identify each.
- The program is dependent on abstract classes not on concrete classes.
- High level modules not dependent on low level modules, additionally details only in low level modules depend on the abstraction.
- Your dependencies point upwards (abstraction)

##Open-Closed Principle (OCP)
- Classes open for extension but closed for modifiable.
- ‘hinge points in a design’ [1], OCD with LSP = DIP.
- ‘…we want to be able to change what the modules do, without changing the source code of the modules’ [2].

##Liskov Substitution Principle (LSP)
Related classes conforming to each other, if:
Sub-typing but no code extension (abstract class/ interfaces)
Code extension but no sub-typing (composition) polymorphism
- Avoiding private variables/ operations in parent/ Super-Type class
- Avoiding implementing new variables/ operations in child class/ Sub-Type
- Over-ridden methods in child/ Sub-Type class accept the same input/ output values as parent/ Super-Type class.

#UML Design
![UML_tick_tac_toe](https://github.com/leakydishes/advanced_algorithms/assets/79079577/9ea832e9-4ae9-4941-90b6-2787d0d704df)


## Does the Design Satisfy the Dependency Inversion principle?
- The program is dependent on abstract classes not on concrete classes and the abstract classes do not depend on detail. Therefore it satisfies the Dependency Inversion Principle.
- I use abstract classes AbstractBoard, Algorithm, AbstractPlayer and AbstractGame which do not contain any details, this reduces dependencies and makes them explicit. Only the concrete classes Board(AbstractBoard), MiniMax(Algorithm), HumanPlayer(AbstractPlayer), BotPlayer(AbstractPlayer) and Games(AbstractGame) contain details. Additionally abstract classes do not depend on any concrete classes as per my UML diagram and code implementation. My classes are also open for extension but closed for modification (OCP).

## Make sure that your use of inheritance is safe. Describe why you preferred to use it an not containment?
- The use of inheritance is safe. As my game uses inheritance in the following:
- AbstractBoard is the common interface (abstract class) for the Board class. Board is a concrete class that represents the board game and inherits from AbstractBoard. This is a ‘is-a’ relationship.
- AbstractGame is the common interface (abstract class) for the Game class. Game is a concrete class that represents the game methods and ‘is-a’ relationship.
- AbstractPlayer is the common interface (abstract class) for the HumanPlayer and BotPlayer. These are concrete classes and both inherit from AbstractPlayer creating the same ‘is-a’ relationship.

### I have used inheritance over containment for the following:
- Code Reusability (AbstractBoard, AbstractGame, AbstractPlayer)
- Structure and Encapsulation (keeps behaviours/methods specific to each class).
- As the behaviours form a ‘is-a’ relationship this is a safe use of inheritance. If there were no shared behaviours then I would have used containment (composition) where class contains an instance of another class as one of its attributes.


### Additional Notes: 
- Inheritance:
o concept of OOP (parent/ Super-Type and derived class – child/ Sub-Type) which can modify parent behaviour.
o  ‘…is-a or is-a-kind’ [1] connection between objects (lecturer, person etc), reduce code duplication. 
1.     Subtype (B is a subtype of A), (book is a subtype of library holding). 
2.     Code Extension to create a new class, write only the differences
  
o   Parent / Super-Type class private, derived child/ Sub-Type class will satisfy the Super-Types specification.
o   Extend the derived class Child/ Sub-Type by adding more functionality

### Sub-Typing vs. Implemented-Inheritance: 
o   *We cannot specify when using inheritance however LSP is used as a principle to guide.
o   Sub-Typing and no Implemented- Inheritance
o   *LSP, make sure dependence exists only on abstract class/ interface. 
 
### Sub-Types are substitutable for Super-Types only if, objects of Sub-Type won’t supervise client by [1],
A.    Failing to satisfy the Super-Types specification.
B.    Having more expectations than the Super-types of specification. 

