# The Christmas tree kata

## Instructions

### Input
Given the children of the world have varying screen sizes, Santa has tasked you with printing a Christmas tree to the console for a given argument of the tree’s height to accommodate for all of the children.

### Output
For example a tree with a height of 2 looks like this:
```
 *
***
 |
```

And a tree with a height of 3 looks like this:

```
  *  
 ***
*****
  |
```

And a tree of height 10:

```
         *  
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
         |
```

# Implementation instructions

We are going to start as simple as possible by hard coding the Christmas tree for the first three levels and then start generelazing it step by step.

- Start writing scenarios for a tree by hard-coding the results first.
   
   1. Let's start with height zero (or even less than zero):
   ```python
    with it("returns empty string when height is zero or less"):
      expect(christmas_tree(0)).to(equal([""]))   
   ```
   
   2. We continue by specifying a tree with height one:
   ```python
    with it("returns a tree when height is 1"):
      expect(christmas_tree(1)).to(equal(["*", "|"]))
   ```
   
   3. We also need a tree with height two:
   ```python
    with it("returns a tree when height is 2"):
      expect(christmas_tree(1)).to(equal([" * ", "***", " | "]))
   ```
   
   4. Finally, to make the generalization a bit easer, we specify a tree with height three:
   ```python
    with it("returns a tree when height is 3"):
      expect(christmas_tree(1)).to(equal(["  *  ", " *** ", "*****", "  |  "]))
   ```
- Now the code probably looks something like this:
  ```python
  def christmas_tree(height):
    if height <= 0: return [""]
    
    if height == 1: 
      return [
        "*", 
        "|"
      ]
    if height == 2:
      return [
        " * ", 
        "***", 
        " | "
      ]
    if height == 3:
      return [
        "  *  ", 
        " *** ", 
        "*****", 
        "  |  "
      ]

  ```
- Let's try to generalize the padding with spaces first
  ```python
  def christmas_tree(height):
    if height <= 0: return [""]
    
    if height == 1: 
      return [
        pad_with_spaces(0, "*"), 
        "|"
      ]
    if height == 2:
      return [
        pad_with_spaces(1, "*"), 
        pad_with_spaces(0, "***"), 
        " | "
      ]
    if height == 3:
      return [
        pad_with_spaces(2, "*"), 
        pad_with_spaces(1, "***"), 
        pad_with_spaces(0, "*****"), 
        "  |  "
      ]
  
  def pad_with_spaces(space_count, stars):
    return space_count * " " + stars + space_count * " "
  ```
- Next, we notice a pattern in how each level is constructed, so we
  extract that in a separate method too:
  ```python
  def christmas_tree(height):
    if height <= 0: return [""]
  
    if height == 1: 
      return [
        generate_layer(1, 1), 
        "|"
      ]
    if height == 2:
      return [
        generate_layer(1, 2), 
        generate_layer(2, 2), 
        " | "
      ]
    if height == 3:
      return [
        generate_layer(1, 3), 
        generate_layer(2, 3), 
        generate_layer(3, 3), 
        "  |  "
      ]
  
  def generate_layer(layer, height):
    return pad_with_spaces(height - layer, "*" * (layer * 2 - 1))

  ```
- Now it is only a matter of adding the stem:
  ```python
  def christmas_tree(height):
    if height <= 0: return [""]
  
    if height == 1: 
      return [
        generate_layer(1, 1), 
      ] + [pad_with_spaces(height - 1, "|")]
    if height == 2:
      return [
        generate_layer(1, 2), 
        generate_layer(2, 2), 
      ] + [pad_with_spaces(height - 1, "|")]
    if height == 3:
      return [
        generate_layer(1, 3), 
        generate_layer(2, 3), 
        generate_layer(3, 3), 
      ] + [pad_with_spaces(height - 1, "|")]
  
  def generate_level(layer, height):
    return pad_with_spaces(height - layer, "*" * (layer * 2 - 1))
  
  def pad_with_spaces(space_count, charstring):
    return space_count * " " + charstring + space_count * " " 
  ```
- This is now easily generalized by
  ```python
  def christmas_tree(height):
    if height <= 0: return [""]
  
    return [generate_layer(i, height) for i in range(1, height + 1)] + [pad_with_spaces(height - 1, "|")]
  
  def generate_level(layer, height):
    return pad_with_spaces(height - layer, "*" * (layer * 2 - 1))
  
  def pad_with_spaces(space_count, charstring):
    return space_count * " " + charstring + space_count * " "
   ```
   
# References

- [Christmas tree kata](https://www.codurance.com/katalyst/build-a-christmas-tree), the original, unmodified kata.
