import os

def clear():
    # Windows
    if os.name == "nt":
        _ = os.system('cls')
    
    # Unix like, linux & macOS
    else:
        _ = os.system('clear')
