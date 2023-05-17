def cheackTime(time):
    if time < 5.0 :
        return print(f"\n\tThat was fast ! You takes only {time} seconds.\n")
    elif time > 25.0 :
        return print(f"\n\tThat was late ! You takes {time} seconds.\n")
    else:
        return print(f"\n\tYou takes {time} seconds.\n")

def cheackScore(total,time):
    if time >= 25.0 :
        total -= 0.25
    if 0.0 >= total :
        return print("\n\tYou didn't get any answer correct!\n")
    elif 0.0 < total < 2.0 :
        return print(f"\n\tUmmm ! You got {total}/5 !\n")
    elif 2.0 <= total < 4.0 :
        return print(f"\n\tNice ! You got {total}/5 !\n")
    elif total >= 4.0 :
        return print(f"\n\tBravo !! You got {total}/5 !\n")