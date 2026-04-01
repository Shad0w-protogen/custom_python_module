def compute(a,b,action): #performs an arithmetic operation,taking in two args and the operation itself.
    operations = {
        "add": a + b,
        "divide": a / b, #made a minor spelling mistake here :3
        "extract": a - b,
        "multiply": a * b,
        "power": a ** b,
    }

    if action in operations:
        return operations[action]
    else:
        raise KeyError

def chaos_int(a,b):
    return int((a + (a**b)) - b)

def chaos_float(a,b): #use on your own risk
    return float((a + (a**b)) - b)

def hi(): #why'd you even need a variable to contain 'hello world'?
    return "Hello World!"

def magic(word): #well no shit
    import time
    """
    Shuffles the letters in a given word without using the 'random' library.
    Uses the current time in microseconds to generate pseudo‑random indices.
    
    Args:
        word (str): The input word to shuffle.
    
    Returns:
        str: The shuffled word.
    """
    if len(word) <= 1:
        return word
    
    # Convert the word into a list of characters for manipulation
    chars = list(word)
    length = len(chars)
    
    for i in range(length):
        # Get current time in microseconds and use it as a seed‑like value
        current_time = time.time()
        microseconds = int((current_time - int(current_time)) * 1_000_000)
        
        # Generate a pseudo‑random index within the valid range
        j = microseconds % length
        
        # Swap characters at positions i and j
        chars[i], chars[j] = chars[j], chars[i]
    
    return ''.join(chars)

def maybe_odd(a):
    print("Number is even" if a % 2 == 0 else "Odd")

