# %%
# How to execute a python function in parallel with a tqdm progressbar?
from multiprocessing import Pool

from tqdm import tqdm
from typing import Any, List

def execute_function_in_parallel(f, arguments: List[Any], verbose: bool = True) -> List[Any]:
    """Executes function *f* in parallel passing in each item in *arguments* as a single argument

    From: https://stackoverflow.com/a/45276885/8488985
    """
    with Pool() as p:
        if verbose:
            results = list(tqdm(p.imap(f, arguments), total=len(arguments)))
        else:
            results = list(p.imap(f, arguments))
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
