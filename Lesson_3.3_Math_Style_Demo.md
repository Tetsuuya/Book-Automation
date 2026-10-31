# LESSON 3.3 — ADDING INTEGERS

## 1. Learning Targets

**Competency:** Grade 7, Quarter 3, Number and Algebra, Competency 9: add integers using concrete counters, pictorial models, and numerals.

**By the end of this lesson, you can:**

- model integer sums with positive and negative counters;
- show integer addition as moves on a number line;
- add integers using the sign rules;
- use number properties to add several integers quickly.

**Essential Questions:** (1) Why does a zero pair equal zero? (2) How does a number line show the sign of a sum? (3) When is a sum of integers negative?

> ### 🎥 INTERACTIVE MULTIMEDIA: Adding Numbers with Different Signs
>
> **Channel:** Khan Academy
> **Direct Link:** [Watch the video](https://www.youtube.com/watch?v=NrVvu7cM8_o)
>
> **Concepts to observe:**
> - Moving right for positive addends and left for negative addends.
> - Why the sum takes the sign of the addend with the larger absolute value.
>
> **Questions:**
> 1. In the video, which direction does a negative addend move you?
> 2. Why can a sum of a positive and a negative number be positive, negative, or zero?
> 3. How could you check a sum using a number line?

**Background.** Many quantities have a direction: a ₱50 deposit and a ₱80 withdrawal, a 3 °C rise and a 5 °C drop. Integers record both the size and the direction of a change. Adding integers finds the **net change**.

## 2. Subtopic 1: Counters and Zero Pairs

A blue counter stands for +1 and a red counter stands for −1. A blue and a red counter together make a **zero pair**.

::: concept KEY CONCEPT: Zero Pair
One positive counter and one negative counter add to zero.
$$ (+1) + (-1) = 0 $$
Adding or removing zero pairs never changes a sum.
:::

To add with counters, put both addends together, circle the zero pairs, and count what is left.

```figure
type: counters
positive: 5
negative: 3
pairs: yes
caption: +5 + (−3). Three zero pairs cancel; two positives remain, so the sum is +2.
```

When both addends have the same sign, there are no zero pairs. Just count all the counters.

```figure
type: counters
positive: 0
negative: 7
caption: −3 + (−4). No zero pairs; seven negatives remain, so the sum is −7.
```

```figure
type: counters
positive: 2
negative: 5
pairs: yes
caption: 2 + (−5). Two zero pairs cancel; three negatives remain, so the sum is −3.
```

| Counters | Expression | Sum |
| :--- | :--- | :--- |
| 5 blue, 3 red | $5 + (-3)$ | +2 |
| 0 blue, 7 red | $(-3) + (-4)$ | −7 |
| 2 blue, 5 red | $2 + (-5)$ | −3 |
| 6 blue, 6 red | $6 + (-6)$ | 0 |

**Quick Check 3.3A**

```exercises cols=3 start=1
Model 4 + (−6) with counters.
How many counters remain in 8 + (−8)?
Model −2 + (−3). Are there zero pairs?
```

## 3. Subtopic 2: Adding on a Number Line

Start at the first addend. Move **right** for a positive addend and **left** for a negative addend. The point where you stop is the sum.

```figure
type: numberline
range: -6, 6
point: -2, start
hop: -2, 3, +5
point: 3, end
caption: −2 + 5 = 3. Start at −2 and move 5 units right.
```

```figure
type: numberline
range: -8, 4
point: 2, start
hop: 2, -5, −7
point: -5, end
caption: 2 + (−7) = −5. Start at 2 and move 7 units left.
```

```figure
type: numberline
range: -9, 2
hop: 0, -3, −3
hop: -3, -7, −4
point: -7, sum
caption: (−3) + (−4) = −7. Two moves to the left.
```

| Expression | Start | Move | Stop (sum) |
| :--- | :--- | :--- | :--- |
| $-3 + 7$ | −3 | 7 right | 4 |
| $2 + (-5)$ | 2 | 5 left | −3 |
| $-4 + (-2)$ | −4 | 2 left | −6 |
| $6 + 0$ | 6 | no move | 6 |

**Quick Check 3.3B**

```exercises cols=3 start=1
Describe the moves for −5 + 9.
Find −3 + (−4) on a number line.
Where do you stop for 6 + (−6)?
```

## 4. Rules and Worked Examples

::: concept KEY CONCEPT: Rules for Adding Integers
**Same signs:** add the absolute values and keep the common sign.
$$ (-a) + (-b) = -(a + b) $$
**Different signs:** subtract the smaller absolute value from the larger, then keep the sign of the number with the larger absolute value.
$$ a + (-b) = a - b, \text{ if } a \ge b $$
$$ a + (-b) = -(b - a), \text{ if } b > a $$
Here a and b are whole numbers.
:::

::: example Worked Example 1 — Two Temperature Drops
**Problem:** The temperature drops 4 °C, then drops another 7 °C. Find the total change.

**Given:** changes of −4 °C and −7 °C   **Find:** the total change   **Rule:** same signs

```figure
type: numberline
range: -12, 2
hop: 0, -4, −4
hop: -4, -11, −7
point: -11, total
caption: Two drops: 4 units left, then 7 more units left.
```

```steps
(-4) + (-7) = -(4 + 7) | same signs: add the absolute values, keep −
= -11 | simplify
```

**Answer:** The total change is **−11 °C**, a drop of 11 °C.
:::

::: example Worked Example 2 — Saving and Spending
**Problem:** A learner saves ₱150, then spends ₱230. Find the net change in the learner's money.

**Given:** +150 and −230   **Find:** the net change in pesos   **Rule:** different signs

```figure
type: numberline
range: -100, 200, 50
hop: 0, 150, +150
hop: 150, -80, −230
point: -80, −80
caption: Move 150 right, then 230 left. The stop is −80.
```

$$
\begin{aligned}
150 + (-230) &= -(230 - 150) && \text{different signs: subtract, keep the sign of the larger} \\
&= -80 && \text{simplify}
\end{aligned}
$$

**Answer:** The net change is **−₱80**, a decrease of ₱80. This is a change, not a balance: the starting amount is not given.
:::

::: example Worked Example 3 — An Elevator Ride
**Problem:** An elevator starts at basement level −3 and goes up 8 floors. On which floor does it stop?

**Given:** start −3, change +8   **Find:** the final floor   **Rule:** different signs

```figure
type: vnumberline
range: -4, 6
zero: Ground floor
point: -3, start
hop: -3, 5, +8
caption: Start at −3 and move 8 floors up.
```

```steps
-3 + 8 = 8 - 3 | different signs: subtract the absolute values
= 5 | 8 has the larger absolute value, so the sum is positive
```

**Answer:** The elevator stops at **floor 5**.
:::

::: example Worked Example 4 — Adding Several Integers Quickly
**Problem:** Find $(-17) + 25 + 17 + (-5)$.

**Given:** four addends   **Find:** the sum   **Rule:** commutative and associative properties, then the inverse property

```steps
(-17) + 25 + 17 + (-5) = [(-17) + 17] + [25 + (-5)] | regroup opposites and easy pairs
= 0 + 20 | inverse property; different signs
= 20 | identity property
```

**Answer:** The sum is **20**.
:::

## 5. Mathematical Reasoning and Common Misconceptions

::: watchout WATCH OUT — Common Errors
- **Wrong:** −5 + (−3) = −2. **Right:** −8. Both addends move left, so add the absolute values.
- **Wrong:** 3 + (−8) = 5. **Right:** −5. The number with the larger absolute value, −8, is negative.
- **Wrong:** 7 + (−7) = 14. **Right:** 0. Opposites form seven zero pairs.
:::

**Reasoning Challenge.** Without adding, explain why $-14 + 9$ must be negative. Then check whether $9 + (-14)$ gives the same result, and name the property.

## 6. Subtopic 3: Properties and Applications

::: concept KEY CONCEPT: Properties of Integer Addition
$$ a + b = b + a \quad \text{(Commutative)} $$
$$ (a + b) + c = a + (b + c) \quad \text{(Associative)} $$
$$ a + 0 = a \quad \text{(Identity)} $$
$$ a + (-a) = 0 \quad \text{(Inverse)} $$
:::

The order of addends does not change the sum. Both paths below stop at 3.

```figure
type: numberline
range: -4, 6
hop: 0, 5, +5
hop: 5, 3, −2
point: 3, sum
caption: 5 + (−2) = 3.
```

```figure
type: numberline
range: -4, 6
hop: 0, -2, −2
hop: -2, 3, +5
point: 3, sum
caption: (−2) + 5 = 3. Same sum: the commutative property.
```

A vertical number line suits depth and height. Sea level is 0; below sea level is negative.

```figure
type: vnumberline
range: -12, 4, 2
zero: Sea level
point: -6, start
hop: -6, -11, −5
caption: A diver at −6 m descends 5 m more and reaches −11 m.
```

| Step | What to do | Example: $-6 + 10$ |
| :--- | :--- | :--- |
| 1 | Compare the signs | different signs |
| 2 | Compare the absolute values | 10 > 6 |
| 3 | Subtract the absolute values | 10 − 6 = 4 |
| 4 | Keep the sign of the larger | positive |
| 5 | State the sum | 4 |

**Quick Check 3.3C**

```exercises cols=3 start=1
Evaluate −19 + 12.
Group to add 15 + (−9) + 4.
A diver at −6 m descends 5 m. Where is the diver?
```

## 7. Practice

### Basic

```exercises cols=3 start=1
(+8) + (+13)
(−9) + (−6)
(+17) + (−24)
(−35) + (+35)
(−12) + 5
14 + (−6)
(−20) + (−30)
0 + (−18)
(−7) + 19
25 + (−40)
(−11) + (−11)
(−3) + 3 + (−4)
```

### Intermediate

```exercises cols=2 start=13
Find the missing number: (−6) + ☐ = 4
Find the missing number: ☐ + (−9) = −15
(−12) + 7 + (−5)
(−25) + 13 + 25 + (−3)
Draw counters for 4 + (−6), then give the sum.
Show (−5) + (−2) on a number line.
```

### Challenge and Word Problems

19. A submarine is 120 m below sea level. It rises 45 m, then dives 30 m. Where is it now?
20. Ana has ₱250. She spends ₱180, receives ₱75, then spends ₱60. Find her final amount and her net change.
21. The sum of two integers is −3. One of them is 8. What is the other?
22. Without calculating, decide whether (−47) + 38 is positive or negative. Explain, then find the sum.

## 8. Contextual Application: A Three-Day Fund Record

A class fund changes by +₱180 on Monday, −₱245 on Tuesday, and +₱90 on Wednesday. (1) Write the three signed changes. (2) Draw one number-line path for the net change. (3) Find the net change by grouping. (4) Explain why the final balance cannot be found without the starting balance.

**Scoring (15 points):** signed changes, 3; number-line model, 3; correct net change with work, 4; change versus balance explained, 3; conclusion in pesos, 2.

## 9. Exit Ticket and Lesson Summary

**3-2-1 Exit Ticket:** 3 facts about adding integers; 2 mistakes to avoid; 1 way to check a sum.

::: note LESSON SUMMARY
- A zero pair, $(+1) + (-1)$, equals 0.
- On a number line, positive addends move right and negative addends move left.
- **Same signs:** add the absolute values and keep the sign.
- **Different signs:** subtract the absolute values and keep the sign of the larger absolute value.
- Commutative, associative, identity, and inverse properties make long sums easier.
:::

## 10. Formative Assessment

**Items 1–10:** Choose the best answer.

| Item | Question and choices |
| :---: | :--- |
| 1 | What is (−7) + (−5)? [  ] A. −2 [  ] B. 12 [  ] C. −12 [  ] D. 2 |
| 2 | What is 4 + (−9)? [  ] A. −5 [  ] B. 5 [  ] C. −13 [  ] D. 13 |
| 3 | Which sum equals zero? [  ] A. −6 + (−6) [  ] B. 6 + 6 [  ] C. −6 + 3 [  ] D. −6 + 6 |
| 4 | Start at −3 and move 8 units right. Where do you stop? [  ] A. −11 [  ] B. 5 [  ] C. −5 [  ] D. 11 |
| 5 | Which property shows 2 + (−7) = (−7) + 2? [  ] A. Associative [  ] B. Commutative [  ] C. Identity [  ] D. Inverse |
| 6 | Seven blue and ten red counters show which sum? [  ] A. 17 [  ] B. 3 [  ] C. −17 [  ] D. −3 |
| 7 | What is −15 + 0? [  ] A. −15 [  ] B. 0 [  ] C. 15 [  ] D. 1 |
| 8 | What is −20 + 7 + 20? [  ] A. −7 [  ] B. −33 [  ] C. 7 [  ] D. 47 |
| 9 | The temperature is −2 °C and rises 6 °C. What is the new temperature? [  ] A. 4 °C [  ] B. −8 °C [  ] C. 8 °C [  ] D. −4 °C |
| 10 | What is 18 + (−25)? [  ] A. 7 [  ] B. 43 [  ] C. −43 [  ] D. −7 |

**Items 11–15:** Show your work.

11. Use counters to explain why 6 + (−9) = −3.
12. Show −4 + 7 on a number line and state the sum.
13. Find (−18) + 26 + 18 + (−6) by grouping. Name the properties you used.
14. A diver at −12 m rises 5 m, then descends 9 m. Find the final position.
15. Is the sum of a positive and a negative integer always negative? Give three examples.

[PAGE BREAK]

# ANSWER KEY — LESSON 3.3

| Item | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Answer | C | A | D | B | B | D | A | C | A | D |

| Item | Model answer |
| :--- | :--- |
| 11 | Six zero pairs cancel; three red counters remain, so the sum is −3. |
| 12 | Start at −4 and move 7 right; stop at 3. |
| 13 | [(−18) + 18] + [26 + (−6)] = 0 + 20 = 20; commutative, associative, inverse, identity. |
| 14 | −12 + 5 + (−9) = −16; the diver is 16 m below the surface. |
| 15 | No. 5 + (−2) = 3; 2 + (−5) = −3; 5 + (−5) = 0. |

| Practice | Answers |
| :--- | :--- |
| Quick Check 3.3A | 4 blue and 6 red: four zero pairs, −2 remains; 0 counters remain; −5, no zero pairs. |
| Quick Check 3.3B | Start at −5, move 9 right, stop at 4; −7; 0. |
| Quick Check 3.3C | −7; [15 + (−9)] + 4 = 10; −11 m. |
| Basic 1–12 | 21; −15; −7; 0; −7; 8; −50; −18; 12; −15; −22; −4. |
| Intermediate 13–18 | 10; −6; −10; 10; −2; −7. |
| Challenge 19–22 | −120 + 45 + (−30) = −105, so 105 m below sea level; ₱85 left, net change −₱165; −11; negative because 47 > 38, sum −9. |
| Contextual application | 180 + (−245) + 90 = 25: a net gain of ₱25. |
