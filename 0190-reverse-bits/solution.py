def reverseBits(n: int) -> int:
    """
    Reverse bits of a given 32 bits unsigned integer.
    
    Args:
        n: A 32 bits unsigned integer
        
    Returns:
        The reversed 32 bits unsigned integer
    """
    result = 0
    
    for _ in range(32):
        # Extract the least significant bit
        bit = n & 1
        # Shift it to the correct position
        result = (result << 1) | bit
        # Right shift n to process the next bit
        n >>= 1
    
    return result


if __name__ == "__main__":
    # Test case 1
    n1 = 43261596
    output1 = reverseBits(n1)
    print(f"Input: {n1}")
    print(f"Output: {output1}")
    print(f"Expected: 964176192")
    print(f"Test 1: {'PASS' if output1 == 964176192 else 'FAIL'}")
    print()
    
    # Test case 2
    n2 = 2147483644
    output2 = reverseBits(n2)
    print(f"Input: {n2}")
    print(f"Output: {output2}")
    print(f"Expected: 1073741822")
    print(f"Test 2: {'PASS' if output2 == 1073741822 else 'FAIL'}")