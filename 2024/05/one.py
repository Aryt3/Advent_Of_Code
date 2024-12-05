rules, pages = open('input.txt', 'r').read().split('\n\n')

rule_dict = {key: [val for _, val in filter(lambda x: x[0] == key, [i.split('|') for i in rules.split()])] for key in {i.split('|')[0] for i in rules.split()}}

def sort_page(page):
    cur_order = page.split(',')
    status = True

    for iind, ival in enumerate(cur_order):
        for xind, xval in enumerate(cur_order):
            if xval != ival:
                # If rule violation occurs change status to False which will return 0
                if iind > xind and ival in rule_dict.keys() and xval in rule_dict[ival]:
                    status = False

    return int(cur_order[len(cur_order) // 2]) if status == True else 0

sorted_pages = sum([sort_page(i) for i in pages.split()])

print(sorted_pages)