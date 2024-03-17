# Seperate file for simple testing

import reminders as rem

time_a = "12:00pm"
time_b = "13:00"
time_c = "2:00pm"

time_a = rem.string_to_time(time_a)
time_b = rem.string_to_time(time_b)
time_c = rem.string_to_time(time_c)

print(rem.time_to_string(time_a))
print(rem.time_to_string(time_b))
print(rem.time_to_string(time_c))
