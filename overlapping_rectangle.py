# Given the top-right and bottom-left coordinates of two rectangles.
# Find the overlapping rectangle.

def overlapping_rectangle(rect1, rect2):
    rect1_top_right_x = rect1[1][0]
    rect1_top_right_y = rect1[1][1]
    rect1_bottom_left_x = rect1[0][0]
    rect1_bottom_left_y = rect1[0][1]

    rect2_top_right_x = rect2[1][0]
    rect2_top_right_y = rect2[1][1]
    rect2_bottom_left_x = rect2[0][0]
    rect2_bottom_left_y = rect2[0][1]

    if rect1_bottom_left_x < rect2_bottom_left_x < rect1_top_right_x:

        result_bottom_left_x = max(rect1_bottom_left_x, rect2_bottom_left_x)
        result_bottom_left_y = rect2_bottom_left_y
        result_top_right_x = min(rect1_top_right_x, rect2_top_right_x)
        result_top_right_y = min(rect1_top_right_y, rect2_top_right_y)

        result_bottom_left = (result_bottom_left_x, result_bottom_left_y)
        result_top_right = (result_top_right_x, result_top_right_y)


    elif rect2_bottom_left_x < rect1_bottom_left_x < rect2_top_right_x:

        result_bottom_left_x = max(rect1_bottom_left_x, rect2_bottom_left_x)
        result_bottom_left_y = rect1_bottom_left_y
        result_top_right_x = min(rect1_top_right_x, rect2_top_right_x)
        result_top_right_y = min(rect1_top_right_y, rect2_top_right_y)

        result_bottom_left = (result_bottom_left_x, result_bottom_left_y)
        result_top_right = (result_top_right_x, result_top_right_y)

    else:
        result_bottom_left = ()
        result_top_right = ()

    result = (result_bottom_left, result_top_right)

    print(result)


rect2 = ((2, 3), (6, 5))
rect1 = ((5, 4), (7, 6))

overlapping_rectangle(rect1, rect2)

