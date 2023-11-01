### Importing Files and functions
Python contains a very useful function that allows us to split up our code into multiple different files and import them into different files. 
First, create a new file `main.py`, inside this file write function, `generate_list`, that takes two parameters `a` and `b`, and returns a list of 20 random numbers from `a` to `b`. Then create a new file `list_ops.py` in which you should have the following functions (each should always have a parameter for the list, and can be implemented in any way you choose):
1. `count_fives` which returns the count of numbers that are divisible by 5 in a given list. 
2. `list_to_binary` - Converts all the numbers in a given list to binary (you might need to do some research for this one!) (see if you can figure out how to use the `map` function for this one!!)
3. `reverse_list` - Exactly what the name suggests, returns a revered list
4. `sliced_list` - A function with two parameters (as well as the l), `a` and `b`, which returns a slice of a list from `a` to `b`. Make sure to check that `a` and `b` are valid indicies! If they are *not* valid, then just return the list unchanged
5. `list_average` - Returns the average of the list
6. `list_product` - Returns the product of all the values in the list
After creating those functions we are going to add the functions you just made into `main.py`, copy and paste the following line of code below into your `main.py`, right after your import statement for `random`:
```python=
import list_ops
```
Then assign a variable to `generate_list` using any values for `a` and `b` you choose. Now see if you can figure out how to call the `count_fives` function with the list you just created as an arguemnt and assign its output to a new variable. If you're stuck check the hint below
<details> <summary> Hint </summary>

```python=
import list_ops
```
In terms of actually using the function think about how we can call `randint` from `random`

```python=
import random
random_number = random.randint(0, 10)
```
    
</details>

Also similar to how we import other modules, we can import only certain functions from different files. 
+ Try to import only the `list_average` function from `list_ops` and then assign its
<details> <summary> Hint </summary>

```python=
from random import randint
```

</details>

Try using both method of importing functions to use the rest of the functions you wrote in `main.py`.

---

After running that, go back to `list_ops.py` and add in a print statement at the bottom of your file, it can say anyting you want. Then, run `main.py` again, what does it output? Can you figure out why?

 + Here's why: when you import a file from another file in python, python automatically runs the code in the file you're importing in order to allow you to be able to access the functions (and variables) in that file, and as you just saw this can cause unwanted side effects. 

+ How do we stop this from happening: Theres a few things we can do to prevent this behavior. 
    1. The first is to try not to leave any "loose" code out in our file. This means that (with a few specfic exeptions) we want mostly all of our code to be contained in functions. Any "loose" code, function calls, and program logic that is neccessary for the program to run should be wrapped in a `main()` function. 
    + An example of a main function might look like this:
    ```python=
def clean_name(name):
    return name.lower().strip() # note that you can chain certain methods as seen here

def clean_age(age):
    while True:
        try:
            return int(age)
        except ValueError:
            age = input("enter a valid number for age: ")

def create_person_list(first_name, last_name, age):
    return [first_name, last_name, age] # create a list with preset values as seen here

def main():
    user_first_name = clean_name(input("Enter your first name: "))
    user_last_name = clean_name(input("Enter your last name: "))
    user_age = clean_age(input("enter your age: "))

    print(f"Person list: {create_person_list(user_first_name, user_last_name, age}"))
```
    2. Next we can use this line of code:
    ```python=
    if __name__ == "__main__":
        # code that only runs when the specfic file it being called
    ```
    What this does is create a conditional that only renders true when the file is not being imported and is being run directly. Think of it this way:
        + If you have an `if __name__ == "__main__"` statement in a file called `login.py`:
            + If you run `login.py` directly (eg `python login.py`), the code inside the if statement will execute
            + If you import `login.py` to a file called `users.py` the if statement will be false, and the code will not run
    In order to see this better, try printing out the variable `__name__` in both `main.py` and `list_ops.py` and see what is outputted.

+  <u>The next challenge </u> is to refactor both `main.py` and `list_ops.py` to include a `main()` function and an `if __name__ == "__main__"` statement! *(For `list_ops.py` your `main()` function should simply just have your two print statements)*
