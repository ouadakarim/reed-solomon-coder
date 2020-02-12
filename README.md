# Reed Solomon Coder

This repository contains of actually two parts. One is related to modular arithmetics.
Then there is the Reed-Solomon Coder which is partially based on the first one.

For each section you can find respective tests in the `/tests` directory. Those will probably explain those concepts
better that I could ever do in this README, so I encourage you to check them out.

# Modular arithmetics

In order to perform basic Modular arithemtic actions you can type:
```
python3 ModularArithmetics.py
```
This way you can either:
 - Add modular numbers.
 - Multiply modular numbers.
 - Find a Modular inverse.
 - Look for Primitives of a certain number.
 - Get to know the Chinese remainder theorem.

# Reed Solomon Coder implementation

If you want to check how a Reed Solomon coder works feel free to check the `main.py` file or directly run it with:
```
python3 main.py
```
For the encoding we use several parameters:
 - n - that's the length of the full encrypted message
 - k - length of the raw message
 - (n-k) is the number of the error correcting symbols
 - Then we also need a primitive polynomial to initialize the coder.

In this script we're starting with a "hello world" message. This message get's encoded with the Reed Solomon coder
but then we corrupt it by injecting on purpose wrong values on the first 6 positions to simulate a grouped error.
Then we decode this message, by additionally providing the information that the values on positions [0, 1, 2] are
invalid, just so that we get under the Singleton bound. Otherwise we would not be able to decode the message in this
specific case. And voila, despite corrupting the message intentionally we were able to resolve the original message.

```
# "hello world" message example
# n = 20
# k = 11
# primitive polynomial = 0x11d

Original: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 145, 124, 96, 105, 94, 31, 179, 149, 163]
Corrupted: [0, 2, 2, 2, 2, 2, 119, 111, 114, 108, 100, 145, 124, 96, 105, 94, 31, 179, 149, 163]
Repaired: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 145, 124, 96, 105, 94, 31, 179, 149, 163]
```

# Reed Solomon "Simplified" vs "Real" Coder
In this repository you'll also find two Reed Solomon Coder implementations. One is the so-called simplified
coder and the other the real one.

You can directly compare them by running the test script with:
```
python3 ReedSolomonTests.py
```
The results will be available in the results.txt file.

