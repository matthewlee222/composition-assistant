# noinspection PyDictCreation
templates = {
    "noeffect": "This statement has no effect. You should remove it, since it has no effect on your program.",
    "commented-code": "You should remove commented-out code from your final product.",
    # "has-one-flag": "Rather than counting the number of times the dice outcome is 1, the code can have a boolean flag "
    #                 "that becomes true when a call to `dice()` is 1. The code can then return the total of outcomes or "
    #                 "1 depending on the boolean flag after the loop.",
    # "extra-nested-loop": "Having this nested loop makes the code more complicated than it should be. Instead, the code "
    #                      "could have a boolean flag that becomes true when a call to `dice()` is 1. At the end, return "
    #                      "the total of outcomes or 1 depending on the boolean flag after the loop. By keeping the "
    #                      "behavior similar to both pig out and non pig out cases, the code is greatly simplified.",
    "simul-assign": "Python supports simultaneous assignment, which would be cleaner to use here. "
                    "e.g.: `a, b, c = 0, 0, 0`",
    "extra-swap": "Rather than using a temporary variable to swap two variables, you can use simultaneous assignment "
                  "e.g. `{first}, {second} = {second}, {first}`",
    "unnecessary-loop-var": "Nice use of a loop here to keep the logic nice and tidy. But as a convention in Python, "
                            "if the name assigned in each loop is not used, we can call it `_` to denote that it's "
                            "really just a placeholder.",
    "ambiguous-variable": "`{original_var_name}` might be ambiguous. A name like `{alternative}` could help clarify.",
    "nice-inline-comment": "Nice use of in-line comments to clarify your logic.",
    "redundant-code": "Notice that you repeat `{repeated_code}` multiple times in your code, which is redundant. "
                      "Consider rearranging your code to avoid such repetition. {hint}",
    # "roll-results-in-list": "This is a very unique approach, I like how you incorporated lists into this! However, in "
    #                         "terms of efficiency, you do not need to keep track of every single roll result in a list, "
    #                         "then search through the list for a `1`; you only need to check if a given roll is a `1` "
    #                         "in every iteration of the loop. This can be done using a boolean and a single `for` loop! "
    #                         "Makes it a little easier on memory and runtime.",
    "spacing": "Remember to use spaces around your operators: `x=0` -> `x = 0`",
    "unnecessary-parens": "Parentheses are not necessary in Python conditionals. You can write `if (X):` as `if X:`",
    # "use-max-function": "Can you use the `max` function to find the correct condition instead of saying "
    #                     "`score1 < goal` and `score0 < goal`?",
    "two-turns-per-iteration": "The code should not run two turns in one iteration. Instead `player` should be used in "
                               "an `if` to figure out which segment of code should be run. Then use the `other` "
                               "function to update the `player` value.",
    # "hardcoded-100": "100 should not be hard-coded as the winning value for the scores. The code should be using the "
    #                  "function parameter `goal`.",
    "multiple-player-comparisons": "The value of `player` can only ever be 0 or 1, therefore instead of two `if`'s "
                                   "this code can be an `if...else` clause instead. "
                                   "Like so: ```if player == 0:\n\t# player 0 stuff\nelse:\n\t# player 1 stuff```",
    "call-expensive-function": "Rather than calling `{expensive_function}` multiple times, it is better to store its "
                               "return value and use it whenever it is needed. This avoids redundant and possibly "
                               "expensive function calls.",
    # "labeled-names": "Nitpick: Since only one of the if clause or the else clause will be entered on each loop "
    #                  "iteration, there's no need to label all your names with the player number. ",
    "incorrect-comments": "While comments can make reading code easier, make sure to keep them consistent with what "
                          "your code actually does!",
    "confusing-helper-functions": "Whenever we define a function, as a programmer, we make a decision to include some "
                                  "information and exclude other information. Here, the code hides some of the game "
                                  "behind helper functions. But the names are both shorthand that requires looking at "
                                  "the body of the function to understand. Especially because the functions are very "
                                  "short, we can instead inline the code in the body of the loop. This way, we can "
                                  "provide better context for what the code does than function names alone.",
    # "call-make-averaged-in-loop": "Since `roll_dice` and `num_samples` do not change in the iteration, the code can "
    #                               "call `make_averaged(roll_dice, num_samples)` outside of the loop and assign it "
    #                               "to a name. Whether it is called outside the loop or within, that name is the "
    #                               "same. This avoids repeating redundant and possibly expensive function calls.",
    # "hardcoded-num-samples": "The number of samples should not be hardcoded as `1000` here. Instead, the name "
    #                          "`num_samples` should be used in case when the function is called a different value is "
    #                          "provided.",
    "while-instead-of-for-loop": "Could you use a `for` loop with `range` here, instead of a `while` loop?",
    "extra-variable": "Reflect on the variable `{extra-variable}`. Is this variable necessary to keep track of? Is "
                      "there a way to achieve the code’s purpose without using it?",
}

typing_test_templates = {
    "repeated-return": "Instead of having the same repeated return statement for each if/elif/else case, how can you "
                       "factor it out of the if/elif/else statements to run at the end of your function.",
    "slice-recursion": "Great use of recursion! Something to think about is that your recursive call makes a copy of a "
                       "sliced list every time. However, each time you slice a list, you have to add all the elements "
                       "to a new list. In the future, think about what that means in terms of efficiency. Is there an "
                       "simpler way to do this with iteration instead?",
    "unnecessary-strip": "It is not necessary to call `strip` if you are calling `split` with no other argument.",
    "unnecessary-full": "Because our iteration will compare each of the words inside the shortest list (between the "
                        "original and the typed), it would consider the case in which someone scores full points. Thus "
                        "this base case is unnecessary.",
    "good-min-key": "Nice use of the min function with a key! This makes the code not only efficient, but easy to read "
                    "and understand.",
    "no-min-key": "Consider using `min` with a key, rather than using a for loop.",
    "extra-list": "Generally, if there is a simpler way to solve without creating an extra list or dictionary, this "
                  "way is preferable because it reduces complexity. How could you use min with a key function to help "
                  "here?",
    "deep-lookahead": "Don’t try to look more than one character ahead - let the recursion handle this.",
    "complex-base-case": "Some of your base cases can be simplified - if both words are still nonempty, can you "
                         "continue to recurse?",
    "repeated-key-dist-calls": "Don't call `get_key_distances()` on every function invocation, as it is expensive to "
                               "call - instead, use the provided variable `KEY_DISTANCES`.",
    "if-instead-of-min": "You can use min, rather than a series of if statements, to compute the desired value.",
    # "use-zip": "Consider using `zip` to iterate over two sequences simultaneously.",
    "not-instead-of-empty-comp": "You can use `not` to test if a string is empty, rather than comparing it to the "
                                 "empty string.",
    "extra-index-variable": "Consider iterating through `words_list` directly, rather than introducing an extra "
                            "index variable that is not necessary",
    "duplicated-loops": "Notice that this `for` loop is repeated multiple times in this function in the various "
                        "branches of your conditional. Consider moving it outside the conditional, and compute the "
                        "argument to `range` using `min`!",
    "long-line": "This line is very long! Consider computing some of its subexpressions and storing their values in "
                 "separate variables first, rather than doing everything in the same line.",
    "weird-append": "Rather than appending to an output list, consider computing the wpm and accuracy in separate "
                    "variables, and constructing the output list from the two variables only at the end when you "
                    "return."
}

templates.update(typing_test_templates)

templates["custom"] = None


def template_completer(text, state):
    cnt = 0
    out = set()
    for key in templates:
        if key in out:
            continue
        if key.startswith(text.strip()):
            if cnt == state:
                return key
            out.add(key)
            cnt += 1

    if out:
        return

    for key in templates:
        if key in out:
            continue
        for word in text.split("-"):
            if word and word in key.split("-"):
                if cnt == state:
                    return key
                out.add(key)
                cnt += 1
                break

    return None
