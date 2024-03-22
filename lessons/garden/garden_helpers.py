"""Some functions for my garden."""

__author__ = "730569217"


def add_by_kind(garden: dict[str, list[str]], type: str, plant: str) -> None:
    """Adding plant by kind."""
    if type in garden:
        garden[type].append(plant)
    else:
        garden[type] = []
        garden[type].append(plant)

     
def add_by_date(month: dict[str, list[str]], date: str, plant: str) -> None:
    """The date the seeds were planted in."""
    if date in month:
        month[date].append(plant)
    else:
        month[date] = []
        month[date].append(plant)


def lookup_by_kind_and_date(garden: dict[str, list[str]], date: dict[str, list[str]], plant: str, month: str) -> str:
    """Look up a kind of plant in date."""
    assert plant in garden
    assert month in date
    plant_list: list[str] = garden[plant]
    month_list: list[str] = date[month]
    lookup: list[str] = []

    for plant in plant_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in both plant_list and month_list
                lookup.append(plant)

    if len(lookup) > 0:
        return f'{plant}s to plant in {month}: {lookup}'
    else:
        return f'No {plant}s to plant in {month}.'

                
