open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def validate_brackets(str):
    stack = []
    for i in str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            x = close_list.index(i)
            if (len(stack) > 0) and (open_list(x) == stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
