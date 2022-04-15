from datetime import date


# To do:

# - get users loc from ip json in order to remove console input requirement. print "You are in x hemisphere and the season is y"

class get_season():

    def get_season_N(day):
        spring_start = 79
        summer_start = 171
        fall_start = 263
        today = day
        if spring_start <= today < summer_start:
            print("Spring")
        elif summer_start <= today < fall_start:
            print("Summer!")
        elif fall_start <= today:
            print("Fall")
        else:
            print("Winter")

    def get_season_S(day):
        fall_start = 79
        winter_start = 171
        spring_start = 263
        today = day
        if fall_start <= today < winter_start:
            print("Fall")
        elif winter_start <= today < spring_start:
            print("Winter")
        elif spring_start <= today:
            print("Spring")
        else:
            print("Summer!")

    day = int(date.today().strftime("%j"))

    print(" ==================\n", " SEASON  DETECTOR\n", "==================\n")
    print("Are you in the northern hemisphere or southern hemisphere?  [N = North | S = South]")
    modifier = input()

    if modifier == str("N") or modifier == str("n"):
        get_season_N(day)
    elif modifier == str("s") or modifier == str("S"):
        get_season_S(day)

if __name__ == "__main__":
    get_season()


