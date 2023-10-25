def pad_with_spaces(content, space_count):
    return space_count * " " + content + space_count * " "


def generate_layer(star_count, space_count):
    return pad_with_spaces("*" * star_count, space_count)


def christmas_tree(height):
    tree = [generate_layer(2 * i - 1, height - i) for i in range(1, height + 1)]
    return tree + [pad_with_spaces("|", height - 1)]
