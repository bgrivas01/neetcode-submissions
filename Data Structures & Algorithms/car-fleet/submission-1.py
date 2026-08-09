class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #pair car position with speed
        pair = [(p,s) for p,s in zip(position, speed)]
        #sorted the cars in decending order
        pair.sort(reverse = True)

        stack = []
        #for each car in pair:
        # - compute the time it takes to reach the target
        # - push that time into a stack
        # - if the new car's time is less than or equal to the time before
        #   it catches up and merges with that fleet -> pop it from stack
        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)