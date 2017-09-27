Three Laws of TDD
=================

* RED - Define the problem with a failing test
* GREEN - Solve the problem
* REFACTOR - Clean up


As test gets more specific code gets more generic

Four Phases
-----------

* Arrange - load data structures.
* Act - Perform the action we want to test
* Assertion - Check the output
* Annihilate - Put the system back to its original state


Naming Tests
------------
Example

Given an Employee
    With PayType of Hourly
        earning $10/hour
    And with 40 hours of Time-CARDS
    And with PayDisposition of PAY MASTER
    And today is Friday

When I Run Payroll

Then the paymaster should have a check for $400

