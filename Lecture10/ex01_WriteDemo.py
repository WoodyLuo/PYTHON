'''
Exercise01 - Write demo Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def main():
    outfile = open("Presidents.txt", "w")
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama")
    outfile.close()


main()
