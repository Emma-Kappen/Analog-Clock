# import library
import pendulum
dt = pendulum.datetime(2020, 11, 27)
print(dt)

#local() creates datetime instance with local timezone
local = pendulum.local(2020, 11,27)
print(local)
print(local.timezone.name)
