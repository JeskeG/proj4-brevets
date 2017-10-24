"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#
ACP = [(200, 15, 34), (200, 15, 32), (200, 15, 30), (400, 11.428, 28), (300, 13.333, 26)]
Special_ends = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    time = arrow.get(brevet_start_time)
    control_dist = control_dist_km
    # Checks for input errors
    if control_dist > 1.2 * brevet_dist_km:
        raise ValueError("This control distance is longer than the brevet distance")
    if not brevet_dist_km:
        raise ValueError("No brevet distance entered")
    if control_dist < 0 or not isinstance(control_dist, float):
        raise ValueError("Control_dist must be an int")
    if control_dist > brevet_dist_km:
        control_dist = brevet_dist_km
    # Calculate like normal
    for dist in ACP:
        distance, min_speed, max_speed = dist
        if control_dist > distance:
            hours = (distance // max_speed)
            minutes = round((distance / max_speed - hours) * 60)
            time = time.shift(hours=hours, minutes=minutes)
            control_dist -= distance
        else:
            hours = (control_dist // max_speed)
            minutes = round((control_dist / max_speed - hours) * 60)
            print(hours, minutes)
            time = time.shift(hours=hours, minutes=minutes)
            return time.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    time = arrow.get(brevet_start_time)
    control_dist = control_dist_km
    # Check for errors
    if control_dist > 1.2 * brevet_dist_km:
        raise ValueError("This control distance is longer than the brevet distance")
    if not brevet_dist_km:
        raise ValueError("No brevet distance entered")
    if control_dist < 0 or not isinstance(control_dist, float):
        raise ValueError("Control_dist must be an int")
    # Special Cases
    if control_dist >= brevet_dist_km:
        return time.shift(hours=Special_ends[brevet_dist_km]).isoformat()
    if not control_dist:
        return time.shift(hours=1).isoformat()
    # Now, if not special, calculate like normal
    for dist in ACP:
        distance, min_speed, max_speed = dist
        if control_dist > distance:
            hours = distance // min_speed
            minutes = round((distance / min_speed - hours) * 60)
            time = time.shift(hours=hours, minutes=minutes)
            control_dist -= distance
        else:
            hours = control_dist // min_speed
            minutes = round((control_dist / min_speed - hours) * 60)
            print(hours,minutes)
            time = time.shift(hours=hours, minutes=minutes)
            return time.isoformat()

