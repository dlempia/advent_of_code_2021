class VentPoint:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class VentLine:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = VentPoint(x1, y1)
        self.p2 = VentPoint(x2, y2)
        self.points = []
        if self.p1.x == self.p2.x:
            if self.p1.y < self.p2.y:
                start_y = self.p1.y
                end_y = self.p2.y
            else:
                start_y = self.p2.y
                end_y = self.p1.y
            step_y = 0
            while (start_y + step_y) <= end_y:
                self.points.append(VentPoint(self.p1.x, start_y + step_y))
                step_y += 1
        elif self.p1.y == self.p2.y:
            if self.p1.x < self.p2.x:
                start_x = self.p1.x
                end_x = self.p2.x
            else:
                start_x = self.p2.x
                end_x = self.p1.x
            step_x = 0
            while (start_x + step_x) <= end_x:
                self.points.append(VentPoint(start_x + step_x, self.p1.y))
                step_x += 1





vent_lines = []
# Load up the Vent Lines
for text_line in open('input5a.txt'):
    text_line = text_line.strip('\n')
    text_line = text_line.replace(' ', '')
    text_line = text_line.split('->')
    point1 = text_line[0].split(',')
    point2 = text_line[1].split(',')
    vent_lines.append(VentLine(int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1])))

point_strings = []
point_count = []
for vent_line in vent_lines:
    for point in vent_line.points:
        point_string = str(point.x) + ',' + str(point.y)
        # print('find string - ' + point_string)
        if point_string in point_strings:
            index = point_strings.index(point_string)
            point_count[index] += 1
            # print('point found! - ' + point_string + ' - index - ' + str(index) + ' - count - ' + str(point_count[index]))
        else:
            point_strings.append(point_string)
            point_count.append(1)
            # print('new point - ' + point_string)

print('point_strings')
# print(point_strings)
# print(point_count)
multi_point_count = 0
for point in point_count:
    if point >= 2:
        multi_point_count += 1
print(str(multi_point_count))




        # print(str(index))
        # print(line_points)
    #     print
    #     # vent_lines.append()
    #
    #     number_calls.append(int(string_number))
# print(number_calls)