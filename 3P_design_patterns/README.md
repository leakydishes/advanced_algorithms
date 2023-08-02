## Tic-Tac-Toe (DIP & OCP) & Minimax Algorithm

#Learning Summary
-	Design patterns which are reusable solutions to common programming problems
-	Designing patterns provides a way to solve and maintain implementation by abstracting details.
-	I explored various creational design patterns (Simple Factory, Factory Method, Abstract Factory, Singleton, and Façade Pattern). 
-	Each creation design pattern has a specific best use of managing object creation.
-	Additionally, I explored frameworks for games and incorporating minimax algorithm using Abstract Factory pattern. This allowed me to create families of objects without specifying concrete classes. 

Simple Factory 
-	A straightforward way to create multiple objects
-	To decouple object creation processes from the main/ client code

Factory Method
-	Create objects, but don’t know exact type of object until runtime
-	Subclasses to alter the object creation process

Abstract Factory
-	Create families of related or dependent objects without specifying their concrete classes

Singleton
-	Ensure a class has only one instance available to all clients/ main
-	Caching, thread pools, registers

Facade Pattern
-	Complex set of classes or library
-	To provide a simplified interface to client/ main
-	Hides complexity and dependencies of the subsystem

Observer:
-	When changes to the state of one object should trigger updates to other objects
-	One to many dependencies between objects
-	State change of one object notifies and updates multiple observer objects


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

## Does the Design Satisfy the Dependency Inversion principle?

- The game is dependent on abstract classes not on concrete classes and the abstract classes do not depend on detail. Therefore it satisfies the Dependency Inversion Principle. 

- I use abstract classes AbstractBoard, Algorithm, AbstractPlayer and AbstractGame which do not contain any details, this reduces dependencies and makes them explicit. Only the concrete classes Board(AbstractBoard), MiniMax(Algorithm), HumanPlayer(AbstractPlayer), BotPlayer(AbstractPlayer) and Games(AbstractGame) contain details. Additionally abstract classes do not depend on any concrete classes as per my UML diagram and code implementation. My classes are also open for extension but closed for modification (OCP).

## Make sure that your use of inheritance is safe. Describe why you preferred to use it an not containment?

- The use of inheritance is safe. As my game uses inheritance in the following:

- AbstractBoard is the common interface (abstract class) for the Board class. Board is a concrete class that represents the board game and inherits from AbstractBoard. This is a ‘is-a’ relationship.

- AbstractGame is the common interface (abstract class) for the Game class. Game is a concrete class that represents the game methods and ‘is-a’ relationship.

- AbstractPlayer is the common interface (abstract class) for the HumanPlayer and BotPlayer. These are concrete classes and both inherit from AbstractPlayer creating the same ‘is-a’ relationship.

#### I have used inheritance over containment for the following:
- Code Reusability (AbstractBoard, AbstractGame, AbstractPlayer)
- Structure and Encapsulation (keeps behaviours/methods specific to each class).

- As the behaviours form a ‘is-a’ relationship this is a safe use of inheritance. If there were no shared behaviours then I would have used containment (composition) where class contains an instance of another class as one of its attributes. ##

### UML Design
![UML_tick_tac_toe](https://github.com/leakydishes/advanced_algorithms/assets/79079577/c6ea8b91-32cf-472c-a983-32ea1ea894ab)

## Reflection
### As seen in the last game play, if the user doesn't select 'smart' paths the bot appears to also not choose the 'smart' path. 
### However when player selects 'smart' paths the bot also selects. 
