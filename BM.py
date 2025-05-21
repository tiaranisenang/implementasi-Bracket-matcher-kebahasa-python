def isBalanced(s: str) -> bool:
    """Memeriksa apakah tanda kurung dalam string s seimbang.

    Args:
        s: String yang akan diperiksa.

    Returns:
        True jika tanda kurung seimbang, False jika tidak."""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack


print(f'"{{([)]}}" -> {isBalanced("{{([)]}}")}')
print(f'"{{[()]}}" -> {isBalanced("{{[()]}}")}')
