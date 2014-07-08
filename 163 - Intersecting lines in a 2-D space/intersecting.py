"""
Descripton:

Given a typical x/y coordinate system we can plot lines. It would be interesting to know which lines intersect.
Input:

A series of lines from 1 to many to put in our 2-D space. The data will be in the form:

(label) (x1 y1) (x2 y2)

    (label) will be a letter A-Z
    (x1 y1) will be the coordinates of the starting point on line
    (x2 y2) will be the coordinates of the ending point on line

example input:

A -2.5 .5 3.5 .5
B -2.23 99.99 -2.10 -56.23
C -1.23 99.99 -1.10 -56.23
D 100.1 1000.34 2000.23 2100.23
E 1.5 -1 1.5 1.0
F 2.0 2.0 3.0 2.0
G 2.5 .5 2.5 2.0

    Max X can be 1,000,000,000.00
    Max Y can be 1,000,000,000.00

Output:

The program will list which lines intersect. And which have 0 intersects.
Example Output:

Intersecting Lines:
A B
A C
A E
A G
F G
No intersections:
D

Difficulty:

This is a coder_d00d(tm) unknown difficulty challenge. It could be easy. Could be hard. But it seems cool for a Friday.

    If you want to make it easier: input is only 2 lines and you return yes/no
    If you want to make it harder: output is the 2 lines and the (x y) point they intersect at.
"""

def get_min(n1,n2):
    if n1 <= n2:
        return n1
    return n2

def get_max(n1,n2):
    if n1 >= n2:
        return n1
    return n2

class Line:
    # Handle infinite slope later.
    def __init__(self, line_str):
        parts = line_str.split()
        self.label = parts[0]
        self.pt1 = (float(parts[1]), float(parts[2]))
        self.pt2 = (float(parts[3]), float(parts[4]))
        if self.pt2[0] - self.pt1[0] == 0:
            self.slope = 'inf'
            self.intercept = 'NaN'
        else:
            self.slope = (self.pt2[1] - self.pt1[1])/(self.pt2[0] - self.pt1[0])
            # Intercept might not actually be on line
            self.intercept = self.pt1[1] - self.slope*self.pt1[0]
    def point_is_on_line(self,pt):
        return (pt[1] == self.slope*pt[0] + self.intercept
                and (get_min(self.pt1[0], self.pt2[0]) 
                             <= pt[0] <= get_max(self.pt1[0],self.pt2[0]))
                and (get_min(self.pt1[1],self.pt2[1]) <= pt[1] 
                     <= get_max(self.pt1[1],self.pt2[1])))


def infinite_version_intersects(line1,line2):
    """
    The lines that we are dealing with in this problem don't continue
    to infinity. A necessary but not sufficient condition for the lines
    in the problem to intersect is that the 'infinite continuations' of
    these lines do intersect. This methods returns the point
    of intersection if these infinite
    continuations do intersect, false otherwise. 
    Note that two infinitely continuing lines intersect if and only if 
    their slope is not equal (or slopes can be equal and they are the
    same lines. 
    """
    if (line1.slope == line2.slope 
        and line1.intercept != line2.intercept):
        return False
    else:
        x_val = (line2.intercept - line1.intercept)/(line1.slope-line2.slope)
        y_val = line1.slope*x_val + line1.intercept
    return (x_val, y_val)


def lines_intersect(line1, line2):
    """
    A necessary and sufficient condition for the two lines to intersect
    is that their infinite continuations must intercept, and the point
    of intersection must be within the domain of the two lines.

    :returns: True if the lines intersect. 
    """
    # Case with two vertical lines (ignoring case same 2 vertical lines
    if line1.slope == 'inf' and line2.slope == 'inf':
        return False
    # Case with one vertical line, one non-vertical
    elif line1.slope == 'inf' or line2.slope == 'inf':
        if line1.slope == 'inf':
            inf_line = line1
            fin_line = line2
        else:
            inf_line = line2
            fin_line = line1
        intersection_x_coord = inf_line.pt1[0]
        intersection_y_coord = (fin_line.slope*intersection_x_coord 
                                + fin_line.intercept)
        return (fin_line.point_is_on_line((intersection_x_coord,
                                           intersection_y_coord)) and 
                get_min(inf_line.pt1[1],inf_line.pt2[1]) 
                <= intersection_y_coord 
                <= get_max(inf_line.pt1[1],inf_line.pt2[1]))
                                 
    # Case with two non-vertical lines that intersect
    elif infinite_version_intersects(line1,line2):
        intersection_point = infinite_version_intersects(line1,line2)
        return ( line1.point_is_on_line(intersection_point)
                 and line2.point_is_on_line(intersection_point))
    # Case of two with same slope. 
    else:
        return False

if __name__ == '__main__':
    with open('lines.txt', 'r') as list_of_lines:
        lines = [Line(line) for line in list_of_lines.readlines()]
    intersecting_lines = []
    lines_present = []
    for i, line in enumerate(lines):
        for j in range(i+1, len(lines)):
            if lines_intersect(line, lines[j]):
                intersecting_lines.append((line.label, lines[j].label))
                lines_present.append(line.label)
                lines_present.append(lines[j].label)
    print "Intersecting Lines:"
    for line in intersecting_lines:
        print line
    print "No intersections:"
    for line in lines:
        if line.label not in lines_present:
            print line.label
