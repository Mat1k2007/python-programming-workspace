# Travel Weather Planner
# A Python script to evaluate travel feasibility based on distance, weather, and transport availability.

distance_mi = 4
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = False

# Evaluate travel conditions and print descriptive status messages
if not distance_mi:
    print("Invalid distance value provided.")
elif distance_mi <= 1:
    if not is_raining:
        print("Travel approved: You can easily walk to your destination.")
    else:
        print("Travel not recommended: It is raining, walking is not suitable.")
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print("Travel approved: Cycling is a great option in these weather conditions.")
    else:
        print("Travel not recommended: Weather or bike availability is not suitable for cycling.")
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print("Travel approved: You can travel using a car or ride-share app.")
    else:
        print("Travel not recommended: Distance is too long and no vehicle is available.")