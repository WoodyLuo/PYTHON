'''
Exercise08 - FootToMeter Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def footToMeter(foot):
    meter = 0.305 * foot
    return meter


def meterToFeet(meter):
    foot = meter / 0.305
    return foot


def main():
    print(format("Feet", '<10s'), format("Meter", '<5s'), " | ", format("Meter", '<10s'), "Foot")
    j = 20
    for i in range(1, 11):
        print(format(i, '<10d'), format(str('%.3f' % footToMeter(i)), '<5s'), " | ",  format(j, '<10d'), str('%.3f' % meterToFeet(j)))
        j += 5


main()
