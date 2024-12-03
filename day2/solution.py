import re
from dataclasses import dataclass
from utils import print_and_time_result, get_input

MAX_LEVEL_DIFF = 3
MIN_LEVEL_DIFF = 1


def parse_input(raw_input: str):
    reports = [list(map(int, line.split())) for line in raw_input]
    return reports


@print_and_time_result(part_num=1, day_num=2)
def part1():
    reports = parse_input(get_input(2))
    reports_safety = []
    for report in reports:
        report_safety = 1
        report_direction = 0
        for curr_level, next_level in zip(report, report[1:]):
            diff = next_level - curr_level
            if not MIN_LEVEL_DIFF <= abs(diff) <= MAX_LEVEL_DIFF:
                report_safety = 0
                break
            curr_dir = 0
            if diff > 0:
                curr_dir = 1
            elif diff < 0:
                curr_dir = -1
            if report_direction != 0 and curr_dir != report_direction:
                report_safety = 0
                break
            else:
                report_direction = curr_dir

        reports_safety.append(report_safety)

    return sum(reports_safety)


@print_and_time_result(part_num=2, day_num=2)
def part2():
    reports = parse_input(get_input(2, test=True))
    reports_safety = []
    for report in reports:
        report_safety = 1
        report_direction = 0
        print(report)
        dampener_active = True
        for curr_level, next_level in zip(report, report[1:]):
            diff = next_level - curr_level
            if not MIN_LEVEL_DIFF <= abs(diff) <= MAX_LEVEL_DIFF:
                if dampener_active:
                    dampener_active = False
                    continue
                report_safety = 0
                break
            curr_dir = 0
            if diff > 0:
                curr_dir = 1
            elif diff < 0:
                curr_dir = -1
            if report_direction != 0 and curr_dir != report_direction:
                if dampener_active:
                    dampener_active = False
                    continue
                report_safety = 0
                break
            else:
                report_direction = curr_dir

        reports_safety.append(report_safety)
    print(reports_safety)

    return sum(reports_safety)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
