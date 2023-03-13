def rps(p1, p2):
    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    result = ['Draw', 'Player 1 won!', 'Player 2 won']
    return result[hand[p1] - hand[p2]]

# print(rps('rock', 'scissors'))
# print(rps('scissors', 'rock'))
# print(rps('rock', 'rock'))


def sum_array(arr):
    # your code here
    return 0 if arr in ([], None) else sum(sorted(arr)[1:-1])

# print(sum_array([1, 2, 4, 6, 2]))
# print(sum_array([]))
# print(sum_array(None))\


def check(seq, elem):
    return elem in seq

# print(check(['t', 'e', 's', 't'], 'e'))
# print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups"))
# print(check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45))
# print(check(["anyone", "want", "to", "hire", "me?"], "me?"))


def digitize(n):
    return map(int, str(n)[::-1])

# a = digitize(35412)
# print(list(a))


def min_max(lst):
    return (min(lst), max(lst))

# print(min_max([1, 2, 3, 4, 5]))


def set_alarm(employed, vacation):
    # return list((locals()).values()) == [1, 0]
    return employed and not vacation

# True if True, True


# print(set_alarm(True, True))  # False
# print(set_alarm(False, True))  # False
# print(set_alarm(False, False))  # False
# print(set_alarm(True, False))  # True


def queue_time(customers, n):
    if customers in (None, []):
        return 0

    n = min(len(customers), n)
    d = {i+1: [] for i in range(n)}

    for c_ in customers:
        queue = list(d.values())
        counter = list(d.keys())
        min_ = counter[queue.index(min(queue))]
        d[min_].append(c_)

    time = sum(max(d.values()))
    for i in list(d.values()):
        print(f"{i} => Sum : {sum(i)}")

    return f"Dict : {d} \nTime Taken : {time}"


# print(queue_time([], 1))
# print(queue_time([5], 1))
# print(queue_time([2, 3, 10], 2))
# print(queue_time([1, 2, 3, 4, 5], 100))
# print(queue_time([2, 2, 3, 3, 4, 4], 2))
# print(queue_time([31, 4, 5, 17, 34, 30, 5, 3,
#       50, 1, 29, 7, 45, 16, 31, 49, 42, 7], 6))


def find_nb(m):
    n, s = 0, 0
    while s < m and s != m:
        n += 1
        s += n**3

        if s == m:
            return n

        elif s > m:
            return -1


# print(find_nb(100))

# print(find_nb(135440716410000))
# print(find_nb(40539911473216))
# print(find_nb(24723578342962))


def rental_car_cost(days):
    rent = days * 40
    d = {
        days < 3: rent,
        days in range(3, 7): rent - 20,
        days >= 7: rent - 40
    }
    print(d)
    return d[True]


# print(rental_car_cost(1))
# print(rental_car_cost(4))
# print(rental_car_cost(7))
# print(rental_car_cost(8))


def points(games):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in games))


# print(points(['1:0', '2:0', '3:0', '4:0', '2:1',
#       '3:1', '4:1', '3:2', '4:2', '4:3']))
# print(points(['1:1', '2:2', '3:3', '4:4', '2:2',
#       '3:3', '4:4', '3:3', '4:4', '4:4']))

def greet():
    return lambda *kwarg: "Hello World!"


def bmi(weight, height):
    b = weight/(height)**2
    return {
        b <= 30.0: "Overweight",
        b <= 25.0: "Normal",
        b <= 18.5: "Underweight",

        b > 30: "Obese"
    }[True]


# print(bmi(50, 1.80))
# print(bmi(80, 1.80))
# print(bmi(90, 1.80))
# print(bmi(110, 1.80))
# print(bmi(50, 1.50))


def wave(people):
    res = []
    for i in range(len(people)):
        lst = list(people)
        if lst[i] != " ":
            lst[i] = lst[i].upper()
            res.append(lst)

    return ["".join(i) for i in res]


print(wave("gap"))
print(wave("codewars"))
print(wave("hello"))
print(wave("two words"))

def hero(bullets, dragon):
    return bullets/2 >= dragon


print(hero(10, 5))  # 10 bullets to defeat 5 draagons
print(hero(7, 4))  # 6/7 bullets can only defeat 3 dragons
print(hero(4, 5))  # 50 bullets which is sufficient enough for defeating dragons
print(hero(100, 40))
print(hero(1500, 751))
print(hero(0, 1))


def count_sheep(n):
    sheep = "".join(f"{i + 1} sheep..." for i in range(n))
