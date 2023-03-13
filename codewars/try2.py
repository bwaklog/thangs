from itertools import permutations as pt


class PagationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

        d = {i + 1: [] for i in range(self.page_count())}
        pg = 1
        for i in self.collection:
            if len(d[pg]) >= self.items_per_page:
                pg += 1
            d[pg].append(i)

        self.distro = d

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        limit = self.item_count() // self.items_per_page
        if self.item_count() % self.items_per_page != 0:
            limit += 1

        return limit

    def page_item_count(self, page_index):
        try:
            return len(self.distro[page_index])
        except KeyError:
            return -1

    def page_index(self, item_index):
        if item_index < 0 or item_index > self.item_count():
            return -1

        item = self.collection[item_index]
        items = list(self.distro.values())
        pgs = list(self.distro.keys())

        for i in items:
            if item in i:
                return pgs[items.index(i)]


# helper = PagationHelper(range(1, 25), 10)
# print(helper.item_count())
# print(helper.page_count())
# print(helper.page_item_count(4))
# print(helper.page_index(23))



def permutations(s):
    l = ["".join(i) for i in list(pt(s))]
    return sorted(list(set(l)))        


print(permutations('aabb'))
