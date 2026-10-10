def build_run_record(
    run_id: str, hyperparameters: list[tuple[str, str]], metrics: list[tuple[str, str]]
) -> dict:
    """
    Build a canonical training-run record.

    run_id: the run's id.
    hyperparameters: (key, value) pairs, in input order, keys may repeat.
    metrics: (key, value) pairs, same shape.

    Return {"run_id": run_id, "hyperparameters": {...}, "metrics": {...}}.
    Within each inner dict, keys are sorted alphabetically. A repeated key
    keeps its LAST value (later pairs overwrite earlier ones). An empty
    list of pairs gives an empty {} for that field, not an omitted key.
    """
    # TODO: build each inner dict first (last-write-wins falls out of plain
    # dict assignment), then rebuild it sorted by key.
    h={}
    for key,value in hyperparameters:
        h[key]=value
    m={}
    for key,value in metrics:
        m[key]=value
    sorted_h=dict(sorted(h.items()))
    sorted_m=dict(sorted(m.items()))
    return {
        "run_id":run_id,
        "hyperparameters":sorted_h,
        "metrics":sorted_m
    }
    pass
