
# Flight Price Booking Heuristic

You get 30 days of flight prices and have to answer a deceptively simple
question:

> "If I want a *good* deal without obsessing over the *perfect* deal,
>  when should I book?"

The trick is that the challenge’s own example already tells you that
“just pick the absolute minimum” is the wrong answer.

---

## Thought process

Take this price list:

```python
[1000, 950, 900, 1100, 850]
````

The cheapest price is `850` on day 4.
But the expected answer is **day 2** (price `900`).

That means whoever wrote the task implicitly wants a policy that balances:

* **Being cheap** – don’t overpay if you don’t have to.
* **Not waiting forever** – if a very good price shows up early, take it.

So instead of pretending we’re building a full forecasting model,
we embrace the real-world behaviour:

> “If the price is close enough to the best I’m likely to see,
> and I already like it, I’ll book.”

---

## Heuristic

1. Look across the 30 days and find the **global minimum** price.
2. Define a **tolerance** around that minimum.

   * Default: 10% above the minimum.
3. Pick the **earliest day** whose price is within that tolerance.
4. If somehow nothing qualifies (pathological input), fall back to the
   day with the absolute minimum.

In symbols:

* Let `p_min` be the minimum price.
* Let `threshold = p_min * (1 + tolerance)`.
* Return the smallest index `i` such that `prices[i] <= threshold`.

For the example:

* `p_min = 850`
* `threshold = 850 * 1.10 = 935`
* First day with price ≤ 935 is day 2 (price 900) → result `2`.

This matches the expected behaviour and encodes the “book early if the
deal is good enough” intuition.

---

## Function

Main function lives in `solution.py`:

```python
def find_best_booking_time(prices, tolerance=0.10):
    ...
```

* `prices`: list of 30 daily prices
* `tolerance`: how picky you are (0.10 = within 10% of best)

The file also includes a tiny `__main__` block that runs the example
from the prompt.

---

## How to run

```bash
python solution.py
```

You’ll see the example prices and the recommended booking day printed
to the console.

---

## Why this is reasonable

* It’s **deterministic** and easy to test.
* The logic is **explainable in one minute** to a non-technical person.
* It matches the sample behaviour without pretending to be a full-blown
  ML model for a toy problem.
