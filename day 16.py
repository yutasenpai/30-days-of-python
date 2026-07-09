# # from datetime import datetime
# # now = datetime.now()
# # print(now)                      # 2021-07-08 07:34:46.549883
# # day = now.day                   # 8
# # month = now.month               # 7
# # year = now.year                 # 2021
# # hour = now.hour                 # 7
# # minute = now.minute             # 38
# # second = now.second
# # timestamp = now.timestamp()
# # print(day, month, year, hour, minute)
# # print('timestamp', timestamp)
# # print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38


# # from datetime import datetime
# # new_year = datetime(2020, 1, 1)
# # print(new_year)      # 2020-01-01 00:00:00
# # day = new_year.day
# # month = new_year.month
# # year = new_year.year
# # hour = new_year.hour
# # minute = new_year.minute
# # second = new_year.second
# # print(day, month, year, hour, minute) #1 1 2020 0 0
# # print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0


# # from datetime import datetime
# # # current date and time
# # now = datetime.now()
# # t = now.strftime("%H:%M:%S")
# # print("time:", t)           # time: 18:21:40
# # time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # # mm/dd/YY H:M:S format
# # print("time one:", time_one)        # time one: 06/28/2022, 18:21:40
# # time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # # dd/mm/YY H:M:S format
# # print("time two:", time_two)        # time two: 28/06/2022, 18:21:40

# # ====================================================================
# # 💻 PYTHON DATE-TIME: DAY 16 EXERCISES
# # ====================================================================

# from datetime import datetime, date, timedelta

# print("="*70)

# # 💡 EXERCISE 1: Extract Current Components
# print("📅 EXERCISE 1: Current Date & Time Breakdowns")

# now = datetime.now()

# print(f"  -Year : {now.year} | Month : {now.month} | Day : {now.day}")
# print(f"  -Hour : {now.hour} | Minutes : {now.minute}")
# print(f"  -Unix timestamp : {now.timestamp()}")
# print("="*70)

# # 💡 EXERCISE 2: Format using strftime (String From Time)
# print("🎨 EXERCISE 2: Formatting Output")

# formatted_now = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(f"  -Standardised format : {formatted_now}")
# print("="*70)

# # 💡 EXERCISE 3: Parse using strptime (String Parse Time)
# print("🧩 EXERCISE 3: Converting Text String Back to Time Object")
# target_string = "5 December, 2019"

# parsed_data = datetime.strptime(target_string, "%d %B, %Y")
# print(f"  -Parsed data is : {parsed_data}")
# print("="*70)

# # 💡 EXERCISE 4: Time left until Next New Year
# print("⏳ EXERCISE 4: Countdown to New Year")

# new_year = datetime(year=now.year + 1, month=1, day=1)
# time_left = new_year - now
# print(f"  -Time left until 1 Jan: {new_year.year}: {time_left.days} days.")
# print("=" * 70)

# # 💡 EXERCISE 5: Time Gap Since Epoch (Jan 1, 1970)
# print("🚀 EXERCISE 5: Gap Since Unix Epoch (1970)")
# start = datetime(1970, 1, 1)
# time_since = now - start
# print(f"   Total days passed since 1970: {time_since.days:,} days")
# print("=" * 70)

# # 💡 EXERCISE 6: Brainstorming Practical Real-World Use Cases
# print("💡 EXERCISE 6: Real-World Use Cases")
# print("   1. Application Logs: Timestamping when a user triggers an event or runs a script.")
# print("   2. E-Commerce Checkouts: Tracking order generation timings and delivery deadlines.")
# print("   3. Scheduling Systems: Creating calendar event alerts, recurring posts, or deadlines.")
# print("=" * 70)

# print("\n🎉 DAY 16 EXERCISES COMPLETED CLEANLY! 🎉\n")