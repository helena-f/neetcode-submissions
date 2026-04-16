class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # to get the starting order, sort the position and corresponding speed 
        tog = []
        for i in range(len(position)):
            tog.append([position[i], speed[i]])
        tog.sort(reverse=True)
        # print(tog)

        # push onto stack each new fleet
        # ie. every time car makes a new fleet, compare with the top of stack
        # if faster, merge
        # if slower, make new fleet
        initial = (target - tog[0][0]) / tog[0][1]
        stack = [initial]

        for pos, s in tog[1:]:
            currtime = (target - pos) / s
            if currtime > stack[-1]:
                stack.append(currtime)

        return len(stack)

        