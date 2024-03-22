in_stock: dict[str, bool] = {"carrots": True, "beets": False}

for key in in_stock:
    if in_stock[key] is True:
        print(key)