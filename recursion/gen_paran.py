def generate_parantheses(num_left, num_right):
    orderings = []
    if num_left <= 0:
        if num_right <= 0:
            return orderings
        else:
            orderings.extend(concat(')',
                             generate_parantheses(num_left, num_right-1)))
    else:
        if num_right < num_left:
            print 'Fatal error: right < left'
            return orderings
        else:
            orderings.extend(concat('(',
                             generate_parantheses(num_left-1, num_right)))
            if num_right > num_left:
                orderings.extend(concat(')',
                                 generate_parantheses(num_left, num_right-1)))
    return orderings

def concat(char, string_list):
    if not string_list:
        return [char]
    return [char + x for x in string_list]

print generate_parantheses(3, 3)
