def get_most_common_enemy(enemies_dict):
    largest = 0

    for name, count in enemies_dict:
        if count > largest:
            largest = count
        else:
            continue

    for name, count in enemies_dict:
        if count == largest:
            return enemies_dict[name]

    return None
