def find_best_booking_time(prices, tolerance=0.10):
    """
    Pick a sane day to book a flight, not the mathematically perfect one.

    Intuition
    ---------
    If you only chase the absolute minimum price, you end up waiting forever
    and stressing over every small change. Real people don't do that.
    A price that's *close enough* to the minimum, but available earlier,
    is usually the smarter move.

    Strategy
    --------
    1. Look at all 30 days and find the cheapest price.
    2. Define a "good enough" band around that minimum: by default, within
       `tolerance` (e.g. 10%) of the best price.
    3. Return the *earliest* day whose price falls inside that band.
    4. If nothing qualifies (strange edge case), fall back to the day with
       the absolute minimum price.

    Example
    -------
    prices = [1000, 950, 900, 1100, 850]
    min_price = 850
    tolerance = 0.10  → threshold = 935

    The first day with price <= 935 is index 2 (price 900),
    so we choose day 2 instead of waiting all the way to day 4.

    Parameters
    ----------
    prices : list[float | int]
        Daily flight prices for the next 30 days.
    tolerance : float, optional
        Allowed relative difference from the global minimum.
        0.10 means "I'll accept up to 10% more than the best price".

    Returns
    -------
    int
        Index (0–29) of the recommended booking day.

    Raises
    ------
    ValueError
        If the price list is empty.
    """
    if not prices:
        raise ValueError("Price list cannot be empty.")

    # Absolute best price (used as our reference point and as a fallback)
    min_price = min(prices)
    min_index = prices.index(min_price)

    # Anything at or below this is considered "good enough"
    threshold = min_price * (1 + tolerance)

    # Grab the earliest day that hits the threshold
    for day, price in enumerate(prices):
        if price <= threshold:
            return day

    # Extremely unlikely, but keeps the function total-order deterministic
    return min_index


if __name__ == "__main__":
    # Quick sanity check with the example from the prompt
    example_prices = [1000, 950, 900, 1100, 850]
    best_day = find_best_booking_time(example_prices)
    print("Prices:", example_prices)
    print("Recommended booking day (0-based):", best_day)
