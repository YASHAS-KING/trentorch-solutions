def chain_assign(original: list) -> dict:
    """
    Given a list `original`, perform the following inside this
    function:
      a = original
      b = a
      c = b

    Return a dictionary with keys "a", "b", "c", "original", each
    mapped to the id() of that variable's referenced object.

    All four values in the returned dictionary should be equal,
    since no new object should ever be created by this function.
    """
    a = original
    b = a
    c = b
    d={}
    d["original"]=id(original)
    d["a"]=id(a)
    d["b"]=id(b)
    d["c"]=id(c)
    return d
    pass
