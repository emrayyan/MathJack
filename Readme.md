# MathJack
A Math-themed card game.

You can use this digital version of MathJack to practice your expression-building skills and understand the gameplay loop. You just need to download the Python (.py) file, run it in VSCode, PyCharm or any suitable IDE and play the demo in the terminal.
A quick overview on the rules for this demo version:

Teams draw from a shuffled deck of digits 1–9 so that they hold five number cards at the start of each question. Played number cards are discarded after each question while unused cards are retained. Not all numbered cards need to be used.

There are five available operations: +, −, ×, ÷ and a ‘concatenation’ operator: ‘|’ (vertical bar). A concatenation operator placed between two number cards makes those cards act like a single two digit number when evaluating the expression. Operations may be reused.

Each question introduces a cap and you have to submit an expression below that cap. An answer above the cap or an invalid expression scores zero. Expressions are evaluated using BODMAS. Non-integer answers are rounded down to the nearest integer.

Any valid expression must:
- Be at most 7 cards long
- Have alternating number and operation cards (remember that concatenation also acts as an operator)
- Start And End with a number card
- Use concatenation operator, ‘|’ at most once

This demo version has five turns, though you can tweak the code to increase that. You can also alter the possible range of cap in the code.

Important Note: This version does not implement any special abilities or a timer.
(you can set up a a timer on your own and come up with your own special abilities to make it more interesting)





