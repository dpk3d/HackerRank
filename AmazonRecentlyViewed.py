"""
TO improve the performance of Recently Viewed items page. we want to implement following functionality.

1. If the item is already on recently viewed items page, it is moved to the top without affecting the
    relative ordering of other items.
2. If item name is not on the recently viewed items, it is added to the top of list.

Starting with empty Recently viewed items page and the given a list of items in the order they viewed,
return the resulting order of the items on the page from top to Bottom.

Note : Two item names are only the same if each of their character is exactly same.

Update the function recentItems. it has following property.
string logs[n]:  the items viewed in chronological order.

Return : final list of item in the recently viewed items page.

logs = [ "book1", "book2", "book3","book1", "book3" ]

"""

def recentItems(list):
    dictionary = {}
    for i, item in enumerate(list):
      # When map is empty
        mx = dictionary.get(item, [-1, 0])
        if mx[0] == -1:
            dictionary[item] = [i, 1]
        else:
            dictionary[item] = [mx[0] + i, mx[1] + 1]

    dataList = [(v, k) for k, v in dictionary.items()]
    dataList.sort(reverse=True)
    return [each[1] for each in dataList]


logs = ["book1", "book2", "book3", "book1", "book3"]
print(" The Recently viewed items are", recentItems(logs))
#  The Recently viewed items are ['book3', 'book1', 'book2']
# This is not optimal solution, it can be enhanced
