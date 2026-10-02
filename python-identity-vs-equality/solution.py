def classify_pair(a, b) -> str:
    """
    Compare a and b using both == and is.
    Return exactly one of these strings:
      "identical"            - a is b (implies == is also True)
      "equal_not_identical"  - == is True but is is False
      "not_equal"             - == is False (is will also be False)
    """
    if a is b:
        return "identical"
    elif a!=b:
        return "not_equal"
    else:
        return "equal_not_identical"
    pass
