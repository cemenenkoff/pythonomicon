"""
Write a function that calculates the angle between the minute and hour clock hands at
any time. Times are given in hours and minutes with military time (e.g. (13, 0) is 1pm).
"""


def get_clock_hands_angle(t):
    h = t[0] % 12
    m = t[1]
    m_tot = m + h * 60
    # The angle between each number is 360 / 12 = 30.
    # The hour hand moves 30 deg / 60 m = 1/2 deg/m.
    # The minute hand moves 360 deg / 60 m = 6 deg/m.
    h_deg = 0.5 * m_tot % 360
    m_deg = 6 * m_tot % 360
    return abs(h_deg - m_deg)


if __name__ == "__main__":
    times = [(0, 0), (6, 30), (12, 0), (9, 30), (3, 15)]
    for t in times:
        theta = get_clock_hands_angle(t)
        msg = f"{t[0]}: {t[1]} -> {theta}"
        print(msg)
