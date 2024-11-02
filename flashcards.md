Q: How do you iterate over a string `s` directly?

A: `for char in s`

Q: How do you iterate over a string `s`, tracking index?

A: `for i, char in enumerate(s)`

Q: How do you iterate over a string `s`, tracking index, index starting from 1?

A: `for i, char in enumerate(s, start=1)`


Q: How do you iterate over a string `s` backwards?

A: `for i in range(len(s) - 1, -1, -1)`
For example, `for i in range(3, -1, -1)` means `i` goes 3, 2, 1, 0.
    - The first number is the number to start *at*.
    - The second number is the number to stop *before*.
    - The last number is the decrement for each pass.

Q: What is *precomputation*?

A: Performing computation before run time to generate a lookup table to be used by an algorithm for optimization.

Q: What is *run time*?

A: The final phase of a computer program's life cycle, the time when code is being executed on the computer's CPU as machine code. It's the running phase of the program.

Q: What is a *lookup table*?

A: It's an array that replaces runtime computation with a simpler array indexing operation, in a process termed as *direct addressing*. A dictionary of key-value pairs is a good simple example.

Q: What is a *hash map*?

A: Firstly, a *hash table* is a data structure that implements an *associative array*, also known as a dictionary or a map. An associative array is an *abstract data type* that maps keys to values. A hash table uses a *hash function* to compute an *index*, also called a *hash code*, into an array of *buckets* or *slots*, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. A map implemented by a *hash table* is called a *hash map*.

Q: What is *direct addressing*?

A: The CPU gets the address directly from the machine code. The address doesn't need to be loaded into a register. This is why lookup tables have O(1) complexity.

Q: What is happening when an address is loaded into a register?

A: The register is temporarily storing the address of a memory location that will be accessed for data.

Q: How are lookup tables different from hash tables?

A: Lookup tables use direct addressing, while hash tables, to retrieve a value $v$ with key $k$, a hash table would store the value $v$ in the slot $h(k)$, where $h$ is a hash function. In other words, $k$ is used to compute the slot for hash tables, while for LUT, the value $v$ is stored in slot $k$, thus directly addressable.

Q: When iterating in reverse, how do you print the previous index?

A: `for i in range(i - 1, -1, -1): print(i + 1)`

Q: What is the knapsack problem?

A:

Q: Given a list of integers, how to find the number of instances of `n`?

A: `mylist.count(n)`

Q: Given a dictionary of string-integer key-value pairs, how do you sort the pairs by integer?

A: `sorted(mydict.items(), key=lambda item: item[1], reverse=True)`

Q: Given a dictionary, how do you get the key with the maximum value?

A: `max(mydict, key=mydict.get)`

Q: Given a dictionary, how do you count the number of items in a list?

A:
```python
counts=dict()
    for i in items:
        counts[i] = counts.get(i, 0) + 1
```

Q: What is a heap?

A:

Q: What is a max/min heap?

A:

Q: Why can't we natively have a max heap in Python?

A:

Q: T/F, every function call "exists" until it returns.

A: True. When we move to a different function call within a function, the old one waits until the new one returns.

Q: T/F, If we want to change immutable data, we don't necessarily need to recreate the entire thing.

A: False, immutable data cannot be changed, so to get a variation, the original must be copied.

Q: T/F, the 10th index of an array is 9.

A: True. The last index is always the length of the array minus 1.

Q: What is the formula for the length of a window?

A: `right - left + 1`

Q: What is amortized analysis?

A: ...

Q: How many subarrays does an array of length n have? Why?

A: (n/2)(n+1) because (n arr of len 1) + (n - 1 arr of len 2) + ... + (1 arr of len n)

Q: What happens with `for i in range(n, n): print(1)`? What about `range(n + 1, n)`?

A: Both times nothing is returned because the range has no elements.

Q: What is the time complexity for concatenating a single character to a string? Hint, strings are immutable.

A: O(n), because the entire string must be replicated first to create a variation.

Q: How do you convert a list of characters into a string? What is the time complexity?

A: `"".join(mylist)`, O(n)

Q: Given `mylist` and indices `j > i`, what is the number of subarrays that end at `j`, starting from `i` or later?

A: `j - i + 1`, the length of the window.

Q: What is the difference between a subarray and a subsequence?

A: Subarrays are contiguous, while subsequences, while maintining their same relative order, needn't be contiguous. (e.g. [1, 3] is a subsequence of [1, 2, 3, 4])

Q: T/F Prefix sums and sliding windows are good for representing array subsequences.

A: False! Prefix sums and sliding windows rely on contiguous subarrays (or substrings, in the case of strings)! Subsequences needn't be contiguous, thus prefix sums and sliding windows aren't applicable (usually dynamic programming is).

Q: What is a subset?
A: A subset is *any* set of elements from an array or string, and the order doesn't matter, meaning that subsets containing the same elements are considered the same (e.g. [1, 2, 4] is the same as [4, 2, 1]).

Q: In general, what is more difficult? Finding a subsequence or a subset of a string?

A: A subsequence is more difficult, because a subset is formed with $n$ random selections, each costing $O(1)$. For a subsequence to be valid, it must maintain the original array's relative order.

Q: When is it ok to sort the order of a subset? What about a subsequence?

A: Subsets can be ordered whenever, since their order doesn't matter. A subsequence shouldn't be sorted unless it's going to be treated like a subset (e.g. the sum of a subsequence).

Q: What is the time complexity of appending to the end of a dynamic array?
A: O(1) amortized. The operation is usually O(1), but sometimes O(n), because dynamic arrays grow in capacity by *doubling* their size when they run out of space. When the dynamic array has space, each operation is O(1). When it needs to grow, a new chunk of memory is set aside, and then all n existing elements must be copied, which takes O(n).

Q: How do you reverse a string most efficiently?
A: `mystr[::-1]`

Q: What would be the algorithmic method to reverse a string from scratch?
A: Use two pointers, converging from the endpoints of the array to meet in the middle.

Q: How do you convert a string of length n to a list of length n?
A: `mylist.split(" ")`

Q: How do you convert a string to uppercase?
A: `mystr.upper()`

Q: T/F, if you convert a list to a set and then back to a list, the relative order of the original list is unchanged.
A: FALSE, when converting to a set (where order doesn't matter), relative ordering may not be preserved!

Q: What is the time complexity for removing duplicates from a list?
A: Amortized O(n), because O(1) for each removal, up to n times in the worst case.

Q: How do you swap the values of `a` and `b`?
A: `a, b = (b, a)`, I add the parenthesis as a reminder that a tuple is being packed on the RHS then unpacked into the LHS, left-to-right.

Q: Explain `mystr[:i:-1]`.
A: Because the -1 indicates reverse, but the first index is omitted, the first index defaults to the index of the last character in the string. That the last index then decrements by 1 until it reaches `i`, finishing the slice.

Q: How do you get the index of the first occurrence of an item in a list?
A: `mylist.index(myitem)`

Q: How do you get the index of the first occurrence of an item in a string?
A: `mystr.index(myitem)`

Q: What is faster, checking for equality, or checking for greater than?
A: The difference is negligible.

Q: How do you get the ASCII value of a character in Python?
A: `ord(ch)`

Q: What does ASCII stand for?
A: American Standard Code for Information *Interchange* (*not* exchange!)

Q: For any given data structure, what's more important to understand, the interface or the implementation?
A: The interface (i.e. valid operations like .append()). How `append()` actually works behind the scenes is less important than knowing how to use it, what it returns (if anything), and it's complexity when called.

Q: What is a hash function?
A: A function $h(k)$ that takes an *input* and *deterministically* converts it into an *integer* that is *less than* a fixed size set by the programmer. Inputs are called *keys*, and the same key will always map to the same integer.

Q: What does `n % m` mean?
A: Remainder after calculating `n` divided by `m`.

Q: For an array, what is the time complexity for accessing a single element at random?
A: $O(1)$

Q: Is a dictionary a hash map? What about the other way around? What about hash table?
A: Yes, they are all the same thing.

Q: What is an ordered data structure?
A: One where insertion order is maintained (i.e. "remembered").

Q: What is an unordered data structure?
A: One where insertion order is not relevant (e.g. a set or a dict).

Q: Why should hash functions use a prime number modulus?
A: See [here](https://stackoverflow.com/questions/1145217/why-should-hash-functions-use-a-prime-number-modulus).

Q: What happens behind the scenes when you have a set and add the same element 100 times?
A: The first time adds it to the set, and the next 99 do nothing.

Q: How to check if a `key` is in a dictionary?
A: `if key in mydict: ...`

Q: How to delete a key from a dictionary?
A: `del mydict[key]`

Q: How to get the keys of a dictionary as an array?
A: `mydict.keys()`

Q: How to get the values of a dictionary as an array?
A: `mydict.values()`

Q: Are `mydict.values()` or `mydict.keys()` generators? lists? What are they?
A: They are dynamically updating "dictionary view" objects.

Q: How does `mydict.keys()` differ from `list(mydict.keys())`?
A: `mydict.keys()`dynamically updates to the current state of `mydict`, while `list(mydict.keys())` is a static snapshot.

Q: How to convert a list into a hash table with empty values?
A: `{k: None for k in mylist}`

Q: What is better for checking for existence? Hash tables or lists?
A: Hash tables or a set determine existence in $O(1)$ whereas lists are $O(n)$.

Q: How to convert a string into a dictionary?
A: `{ch:None for ch in s}`

Q: Is a set a hashmap?
A: Yes, but the keys don't map to anything.

Q: Do hash maps preserve order?
A: No in the vast majority of instances. In *Python* however, since 3.7, dictionaries and sets preserve insertion order, meaning items are iterated in the order they were added.

Q: T/F, in Python 3.7 or later, converting a list to a set will preserve the relative ordering of unique elements in the original list.
A: True!

Q: How to add an item to a set?
A: `myset.add(item)`.

Q: How to delete an item in a set?
A: `myset.remove(item)` raises a KeyError if dne, `myset.discard(item)` does nothing, but both methods accomplish deletion.

Q: Does performing `myset.pop()` remove the rightmost element or an arbitrary element? What about in Python 3.7+?
A: Even in Python 3.7+, `myset.pop()`.

Q: What's the best way to get a value from a dictionary if it exists, otherwise None?
A: `mydict.pop(value, None)`

Q: Is `range(n)` good to use for existence checks?
A: No, it's not optimized for existence checks.

Q: What is a `Collections.defaultdict` in Python, and how does it differ from a `dict`?
A: A `defaultdict` is instantiated with a default *callable* that generates a value for missing keys (rather than raising a KeyError in a regular `dict`).

Q: What is the best way to check that all items in a (nonempty) list are equal?
A: Use a generator expression: `all(i == mylist[0] for i in mylist)`

Q: What is the best way to get the count of all items in a list or string?
A: Use a `collections.Counter` and instantiate it with `Counter(mystr)`.

Q: True or False, `collections.Counter` and `collections.defaultdict` are both subclasses of a `dict`.
A: True, both are like dicts, but have additional functionality for quality of life.

Q: What is the complexity for creating a hash map from an array?
A: O(n)

Q: What is the complexity for converting a hash map's values to a set?
A: O(n)

Q: For simple counting purposes, what is better, `defaultdict` or `Counter`?
A: `Counter` has more overhead due to specialized methods, so it's generally slower than `defaultdict(int)` for simple counting purposes.

Q: T/F a prefix sum of an array of strictly positive integers has distinct values.
A: True! The prefix sum elements are always increasing.

Q: T/F prefix sums of arrays cannot have repeated elements.
A: False, arrays that contain positive and negative numbers can have duplicate prefix sums.
