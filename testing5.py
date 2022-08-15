def clockHandAngles(seconds):
    hours = 0
    minutes = 0
    second = 0
    while seconds > 0:
        if seconds >= 3600:
            hours += 1
            seconds -= 3600
        elif seconds >= 60:
            minutes += 1
            seconds -= 60
        elif seconds <= 59:
            second += 1
            seconds -= 1
        hourDegree = (360/12) * hours
        minuteDegree = (360/60) * minutes
        secondDegree = (360/60) * second
    return f"The hands in degrees hours: {hourDegree} and minutes: {minuteDegree} and seconds: {secondDegree}"


print(clockHandAngles(3674))
