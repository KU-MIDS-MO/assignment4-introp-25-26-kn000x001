import numpy as np

def mask_and_classify_scores(arr):
    """
    write your solution here;
    follow the instructions in the README.
    """
    ### Replace with your own code (begin) ###
    if not isinstance(arr, np.ndarray):
        return None
    if arr.ndim != 2:
        return None
    if arr.shape[0] != arr.shape[1]:
        return None
    if arr.shape[0] < 4:
        return None

    n = arr.shape[0]
    
    cleaned = arr.copy()

    cleaned = np.clip(cleaned, 0, 100)
    
    levels = np.zeros_like(cleaned, dtype=int)

    levels[(cleaned >= 40) & (cleaned < 70)] = 1
    levels[cleaned >= 70] = 2

    row_pass_counts = np.zeros(n, dtype=int)

    for i in range(n):
        count = 0
        for value in cleaned[i]:
            if value >= 50:
                count += 1
        row_pass_counts[i] = count

    return (cleaned, levels, row_pass_counts)
    pass
    ### Replace with your own code (end)   ###
