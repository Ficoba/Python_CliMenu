# Python CliMenu
## Introduction
I created this class to generate & manipulate easily a menu in CLI.

Certainly that other projects or libraries offer this kind of solution.

I admit that I did not search too much on the net because in my opinion it was quite simple to create this kind of object.



I propose this base which can be adapted in other languages. I will make a fork for PowerShell.

You can use, modify, fork, ... This class as you like.

If you have any code improvement tips please let me know I do not have a lot of Python experience.

I am a bit of a dabbler in everything at one time I had a good experience in PHP, but I am a bit rusty since then :-D
## Requirement
import sys
## Compatibility
Python 3.6 or greater

Python 2.7 (I will check on a machien of my job, but I think it is good :-))
## Examples
### Example 1 - Simple menu multi-select
```python
import sys
from CliMenu import CliMenu

mainMenu = CliMenu(title = "Simple menu multi-select")
mainMenu.addOption(label = "Entry 1")
mainMenu.addOption(label = "Entry 2")
mainMenu.addOption(label = "Entry 3")
mainMenu.addOption(label = "Entry 4")
mainMenu.printMenu()

print(mainMenu.getSelectedIndex())
```

### Example 2 - Simple menu unique choice
```python
import sys
from CliMenu import CliMenu

mainMenu = CliMenu(title = "Simple menu unique choice", uniqueChoice = True)
mainMenu.addOption(label = "Entry 1")
mainMenu.addOption(label = "Entry 2")
mainMenu.addOption(label = "Entry 3")
mainMenu.addOption(label = "Entry 4")

mainMenu.printMenu()

print(mainMenu.getSelectedIndex())
```

### Example 3 - Simple menu with auto. commit (no confirmation). But without confirmation
It works similarly to unique choice if select a specific entry.

But we can choose all options.

To disable all options possible add option: uniqueChoice = True
```python
import sys
from CliMenu import CliMenu

mainMenu = CliMenu(title = "Simple menu auto. commit", autoCommit = True)
mainMenu.addOption(label = "Entry 1")
mainMenu.addOption(label = "Entry 2")
mainMenu.addOption(label = "Entry 3")
mainMenu.addOption(label = "Entry 4")
mainMenu.printMenu()

print(mainMenu.getSelectedIndex())
```

### Example 4 - Menu + sub menu
You do not have to use "deepcopy" for the class. I was being lazy for this example :-)
```python
mainMenu = CliMenu(title = "Menu + sub menu")

## Create 1st sub-menu
subMenu = CliMenu(title = "1st sub menu")
subMenu.addOption(label = "Entry 1.1").addOption(label = "Entry 1.2").addOption(label = "Entry 1.3")
## Create 1st entry + sub-menu created before
mainMenu.addOption(label = "Entry 1", subMenu = copy.deepcopy(subMenu))

## Create 2nd sub-menu
subMenu.setTitle("2st sub menu")
subMenu.clearOptions()
subMenu.addOption(label = "Entry 2.1")
subMenu.addOption(label = "Entry 2.2")
subMenu.addOption(label = "Entry 2.3")
## Create 2nd entry + sub-menu created before
mainMenu.addOption(label = "Entry 2", subMenu = copy.deepcopy(subMenu))

mainMenu.addOption(label = "Entry 3")
mainMenu.addOption(label = "Entry 4")

mainMenu.printMenu()

print(mainMenu.getSelected())
print(mainMenu.getSelectedIndex())
print(mainMenu.getSelectedIndexes())
```

## Remarks
### getSelectedIndexes() method
Return a list() containing at least one other list()
Example of result of this method:
> [[1, [0, 1, 2]], [2]]
Description:
```
[
   [
     1,  <== For first menu we have selected this index (2nd choice, because index start to 0)
     [0, 1, 2]  <== If we have a second value then it is a list(), because we have a submenu. Here indexes 0, 1 & 2 have been selected
   ], 
   [2],  <== For first menu we have selected this index (3rd choice). And we have no other value. In this case we have no submenu
   [
     3,  <== For first menu we have selected this index (4th choice)
     []  <== If we have a second value then it is a list(), because we have a submenu. Here no choice has been made because this list is empty
   ]
]
```
I think for more simplicity I suggest to use: getSelected() & check if there is a sub-menu & use again getSelected() recursively for each sub-menu found.

I implemented getSelectedIndexes(), because it did not require a great deal of effort on my part and for the fun of it :-)
