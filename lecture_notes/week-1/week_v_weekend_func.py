def week_v_weekend(day):
    '''Check if a day is a weekend day; if not, say it is a week day'''
    day_lower = day.lower()
    if day_lower in ["saturday", "sunday"]:
        return "It's the weekend!"
    else:
        return "It's a weekday!"
