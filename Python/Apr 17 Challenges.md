
# 🐍 Python Challenge List (Level 1 → 4)

Welcome to Apr 17 2025  Python challenges!   
The questions get **progressively harder**, so take your time, think carefully, and don't rush.  

---

## 1. Sum of Even Numbers (Easy Warmup)

**Problem:**  
> Write a function that takes a list of numbers and returns the sum of all even numbers in the list.

**Example:**
```python
Input: [1, 2, 3, 4, 5, 6]
Output: 12
```
> (Because 2 + 4 + 6 = 12)

**Explanation:**
- Loop through the list.
- Check if a number is even (`number % 2 == 0`).
- Add all even numbers to a total sum and return it.

**Tip:**  
> Focus on clean and readable code. Try to do it in one line using list comprehension if you feel brave.

---

## 2. Find the Missing Number (Medium)

**Problem:**  
> You are given an array containing `n` distinct numbers taken from `0, 1, 2, ..., n`. One number is missing. Find the missing number.

**Example:**
```python
Input: [3, 0, 1]
Output: 2
```

**Explanation:**
- Sum of first `n` numbers is `n*(n+1)//2`.
- Calculate expected total.
- Subtract the actual array sum from it to find the missing number.

**Tip:**  
> Don't overcomplicate it. Think mathematically — not everything has to be brute force.

---

## 3. Group Anagrams Together (Harder Logic)

**Problem:**  
> Given a list of words, group them together if they are anagrams (words formed by rearranging letters).

**Example:**
```python
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

**Explanation:**
- Sort each word alphabetically.
- Use a dictionary with the sorted word as the key.
- Group words based on their sorted version.

**Tip:**  
> If it feels messy, draw it out: map how "eat" → "aet" and "tea" → "aet". Visualizing mappings helps a LOT.

---

## 4. Decode a String (If You Solve This, You’re Him 🔥)

**Problem:**  
> Given an encoded string like `"3[a2[c]]"`, return its decoded version.

**Example:**
```python
Input: "3[a2[c]]"
Output: "accaccacc"
```

**Explanation:**
- `2[c]` ➔ `cc`
- `a2[c]` ➔ `acc`
- `3[acc]` ➔ `accaccacc`
- Use a **stack** to decode nested structures.

**Tip:**  
> Break it down layer by layer. Every time you see a `]`, think: "what just finished?" Then build from the inside out.

---

# 🧠 Final Tips:

- **Level 1 and 2:** Don't overthink it. Write something simple that *works first*, then polish.
- **Level 3:** Organize your thoughts. Grouping logic is all about **smart mapping**.
- **Level 4:** If it feels hard, GOOD. That's exactly where you start leveling up.  
- **Most important:** **NEVER** copy-paste the first StackOverflow solution you see. Force your brain to cook 🔥.

---

Happy Coding, DEV! 👨‍💻🚀  
_The grind now will pay off later. Trust._

