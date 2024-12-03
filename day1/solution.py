from utils import print_and_time_result, get_input
from collections import Counter
from functools import reduce


def parse_input(raw_input: str):
    ls = []
    rs = []
    for line in raw_input:
        l, r = line.split()
        ls.append(int(l))
        rs.append(int(r))

    return ls, rs


@print_and_time_result(part_num=1, day_num=1)
def part1():
    left_list, right_list = parse_input(get_input(1))
    distances = [abs(l_num - r_num) for l_num, r_num in zip(sorted(left_list), sorted(right_list))]

    return sum(distances)


@print_and_time_result(part_num=2, day_num=1)
def part2():
    left_list, right_list = parse_input(get_input(1))
    right_counter = Counter(right_list)
    return reduce(lambda acc, el: acc + right_counter[el] * el, left_list, 0)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
