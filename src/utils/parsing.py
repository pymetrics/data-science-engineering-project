"""
Util functions for parsing data inputs
"""

def parse_options(**kwargs):
    opts = [(k, v) for k, v in kwargs.items() if v is not None]
    if len(opts) != 1:
        raise ValueError("Exactly one input data type must be provided, got %d" %(len(opts)))
    return opts[0]
