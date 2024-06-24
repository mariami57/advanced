input_line = [[char for char in part.split()] for part in input().split("|")]
[print(*backwards, end=" ") for backwards in input_line[::-1] if backwards]