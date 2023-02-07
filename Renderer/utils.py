def in_rect(target_x, target_y, source_x, source_y,  width, height):
    if source_x < target_x < source_x + width and source_y < target_y < source_y + height:
        return True
    return False
