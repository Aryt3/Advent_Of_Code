rules, pages = open('input.txt', 'r').read().split('\n\n')

# Parse Rules into dictionary
rule_dict = {key: [val for _, val in filter(lambda x: x[0] == key, [i.split('|') for i in rules.split()])] for key in {i.split('|')[0] for i in rules.split()}}

# Rule Violation Check Function
def violates_rule(cur_order):
    for left, right_list in rule_dict.items():
        for right in right_list:
            # If left appears after right, it's a violation
            if left in cur_order and right in cur_order:
                if cur_order.index(left) > cur_order.index(right):
                    return left, right  
    return None

# Sorting Function
def sort_page(page):
    cur_order = page.split(',')

    if not violates_rule(cur_order):
        return 0  # Return 0 if no violations

    while True:
        violation = violates_rule(cur_order)
        if not violation:
            break 

        # Get indices of the violating pair
        left, right = violation
        left_idx = cur_order.index(left)
        right_idx = cur_order.index(right)

        # Swap left and right to fix the order
        cur_order[left_idx], cur_order[right_idx] = cur_order[right_idx], cur_order[left_idx]

    # Get the middle element of the sorted list
    middle_element = cur_order[len(cur_order) // 2]
    return int(middle_element)

# Gather all pages
sorted_pages = sum(sort_page(page) for page in pages.split('\n') if page.strip())

print(sorted_pages)
