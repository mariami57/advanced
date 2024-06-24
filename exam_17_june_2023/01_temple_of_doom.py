from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while challenges and tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_substance * current_tool
    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)


if (not tools or not substances) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
elif not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print("Tools:", end=" ")
    print(*tools, sep=", ")
if substances:
    print("Substances:", end=" ")
    print(*substances, sep=", ")
if challenges:
    print("Challenges:", end=" ")
    print(*challenges, sep=", ")