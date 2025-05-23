# oops

"""
Class:

    - class is a blueprint or tempalate for creating objects
    - It defines set of attributes (data) and methods (functions). attributes can called properties
    - when we create class don't allocate memory. when we create object while allocate memory
    - create steps:
        - use class keyword and CLASS_NAME for class create. eg:  class TestClass:
        - next create constructor use def __init__(self): it for creations 
        - self like a this keyword. can access  self.PROPERTIES_NAME
        - can create fucntions inside class
        - self is must declare in constructor


Object:
     
    - Object is a instance of class
    - which contains data and methods defined by its class
    - class have multiple object
    - eg: t1 = TestClass()
    - python will pass t1 for identify which object is actually background process is - t1.METHODS_NAME(t1)
    - when the object is create immediately called constructor
    - can access properties by object


Inheritance:

    - inheritance is oop one class access to another class attributes and methods
    - child class access to parent class 
    - child class can reuse code from parent class and modify or extend that methods
    - if want to inhertance use () parenthesis and pass class which class we needed

        single inheritance:
            - just call single class to inside the class arguments eg : CLASS_NAME(INHERITANCE_CLASS)

        Multiple inheritance:
            - if passed multiple classes its called mulitple inheritance eg : CLASS_NAME(INHERITANCE_CLASS_1, INHERITANCE_CLASS_2)

        Multilevel inheritance:
            - the classes access by level child can access parent and parent can acces grandparent

* if inheritance works by MRO - method resource order its a mechanisum execution order flow

* keywords - __init__ , self, super(), () and if any class access to another class we must use super()

Abstraction:

    - Hiding the complexity implementation details of the system
    - exposing only essentials features only to the user
    - The class not instantiated : can't create object in abstract class
    - Abstruct class should one or more abstract methods
    - can create methods in abstract class but won't implementation in abstract class
    - Implement abstract methods in subclass - like inheriting subclass to base class there will implement methods

* if want use abstrct method , we should import- from abc import ABC , abstrctmethod
* ABC pass to class parameter it's called abstract class - eg class TestClass(ABC)
* atleast present one methods in abstract class - eg @abstractmethood
* No implementation only declaration sections present
* it's overwrtie methods
* whenever you have mentioned abstract methods in abstract class. the child class should be overwrite methods (you should declare methods)

    usecase:
        - if share any code to others. we don't share implementaions sections. just share abstarct methods only
 
access modifiers:

    - abstract, static, class

Encapsulation:

* it refers to the  bundling the data (attributes)and methods(methods)
* access protection - don't access data outside class or anyone
* It operates data into single unit as a class
* restrcitng access to certain the deatils of the object and can access by well defined interface methods

access specifiers:

    - it applicable for variables and functions
    - in python don't strictly follow
    - public, protected, private
    - public varibles default
    - protected varible is before add single _ it's called protected variable eg : _var1
    - private variable is before add double __ it's called private avriable eg: __var1

* if want access private varibles you can access by name mangling it can access using _CLASSNAME__VARIABLE_NAME

* The encapsulation is compained access modifier and access specifier
* we can prevent varibles and methods
* the encapsulation contains private and protected public variables and methods. the functions access with some restrictions


* we can access well defined functions we can access throgh defined public functions - its a access modifiers


Polymorphism:

* In object-oriented programming, polymorphism allows different classes to define methods with the same name, but with different implementations.

* it allows a differnt classes to be treated as instance of the same class through the common interface
* Its enables methods called by differnt type of objects, promoting, scalbilty, flexibilty

* single method but differnt behaviour
* 


- method overriding - two diffent class not in the same class

- In java overloading : same method differ arguments
- In python don't overloading concept


usecase:

    - code reusable
    - code maintainabilty, readability
    - recommend large or complexity applications

"""