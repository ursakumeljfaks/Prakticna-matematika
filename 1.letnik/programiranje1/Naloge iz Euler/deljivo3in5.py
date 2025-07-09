def poglejmo(n):
    """vrne seštevek n števil, ki so deljiva s 3 in s 5."""
    vsota = 0
    n = n - 1
    while n != 0:
        if n % 3 == 0 or n % 5 == 0:   
            vsota += n
        n -= 1
    return vsota 
  


        
    
