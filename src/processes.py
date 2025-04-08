def some_logic(data:dict[str, list[float]]):
    """Función que hace operaciones"""
    print(f"{data=}")
    sum_x = sum(data["x"])
    sum_y = sum(data["y"])

    if not sum_x:
        return 0
    return sum_y/sum_x