from collections import deque
size = deque(int(x) for x in input().split(", "))
paper = deque(int(x) for x in input().split(", "))
boxes = 0
while size and paper:
    current_size = size.popleft()
    current_paper = paper.pop()
    if current_size <= 0:
        paper.append(current_paper)
        continue
    elif current_size == 13:
        first_paper = paper.popleft()
        paper.appendleft(current_paper)
        paper.append(first_paper)
        continue
    else:
        result = current_paper + current_size
        if result <= 50:
            boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if size:
    print(f"Eggs left: {', '.join(str(x) for x in size)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")