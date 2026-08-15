# -*- coding: utf-8 -*-
"""Fill intermediate metric rows between start/end App samples."""
from datetime import datetime


class App:
    def __init__(self, name, time, s1, s2, s3, s4, s5):
        self.name = name
        self.time = time
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5


def parse_time(value):
    """Accept YYYYMMDD or YYYYMM."""
    text = str(value)
    if len(text) == 6:
        return datetime.strptime(text, "%Y%m")
    return datetime.strptime(text, "%Y%m%d")


def format_time(dt, template):
    text = str(template)
    if len(text) == 6:
        return dt.strftime("%Y%m")
    return dt.strftime("%Y%m%d")


def read_data():
    app1 = App("1", "20210501", 1.0, 1.0, 1.0, 1.0, 1.0)
    return [app1]


def handle(app_list):
    return app_list


def handle_app(app_start, app_end, steps=5):
    """
    app1:[start, end] ==> app1:[start, start+1, ..., end]

    Linearly interpolate s1..s5 across `steps` intervals between start and end.
    """
    start_dt = parse_time(app_start.time)
    end_dt = parse_time(app_end.time)
    if end_dt <= start_dt or steps <= 0:
        return [app_start, app_end]

    result = []
    delta = (end_dt - start_dt) / steps
    for i in range(steps + 1):
        ratio = float(i) / steps
        dt = start_dt + delta * i
        result.append(
            App(
                app_start.name,
                format_time(dt, app_start.time),
                lerp(app_start.s1, app_end.s1, ratio),
                lerp(app_start.s2, app_end.s2, ratio),
                lerp(app_start.s3, app_end.s3, ratio),
                lerp(app_start.s4, app_end.s4, ratio),
                lerp(app_start.s5, app_end.s5, ratio),
            )
        )
    return result


def lerp(start, end, ratio):
    return start + (end - start) * ratio + noise()


def noise():
    return 0.01


def calc_s(start, end, steps=5):
    return [lerp(start, end, float(i) / steps) for i in range(steps + 1)]


def write_data(app_list):
    for app in app_list:
        print(
            "{},{},{},{},{},{},{}".format(
                app.name, app.time, app.s1, app.s2, app.s3, app.s4, app.s5
            )
        )


def main():
    read_list = read_data()
    write_list = handle(read_list)
    write_data(write_list)


if __name__ == "__main__":
    main()
