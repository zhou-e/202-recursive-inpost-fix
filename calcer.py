import stacks

operands = { '^' : 2,
'~' : 2,
'*' : 1,
'/' : 1,
'+' : 0,
'-' : 0}

def infix_to_postfix(ifexp):
    ifexp = ifexp.split(' ')
    master = stacks.StackArray()
    master.push(stacks.StackArray())
    nums = []
    recs = 0
    for i in range(len(ifexp)):
        if ifexp[i] == '(':
            master.push(stacks.StackArray())

        elif ifexp[i] == ')':
            length = master.arr[master.size()-1].size()
            for j in range(length):
                nums.append(master.arr[master.size()-1].pop())
            master.pop()

        elif ifexp[i] in operands:
            length = master.arr[master.size()-1].size()
            if master.arr[master.size()-1].size() > 0 and \
               operands[master.arr[master.size()-1].arr[length-1]] > operands[ifexp[i]]:
                for x in range(master.arr[master.size()-1].size()):
                    nums.append(master.arr[master.size()-1].pop())
            master.arr[master.size()-1].push(ifexp[i])

        else:
            nums.append(ifexp[i])
            if master.size() > 1 and len(nums) > 1 and master.arr[master.size()-1].size() > 0:
                length = master.arr[master.size()-1].size()
                if i+1 < len(ifexp) and ifexp[i+1] != ')' and \
                   (not master.arr[master.size()-1].arr[length-1] in '+-~' \
                   or not operands[ifexp[i+1]] > 0): 
                    nums.append(master.arr[master.size()-1].pop())
                
    if master.arr[0].size() > 0:
        for i in range(master.arr[0].size()):
            nums.append(master.arr[0].pop())
    return ' '.join(nums)

def pstfix_eval(pfexp):
    pass

def postfix_valid(pfexp):
    pfexp = pfexp.split(' ')
    nums = ops = 0
    for item in pfexp:
        if item in operands and not item == '~':
            ops += 1
        elif item != '~':
            nums += 1
        if ops >= nums:
            return False
    return True
