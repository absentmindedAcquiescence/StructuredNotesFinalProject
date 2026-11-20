# 4. Expanded greeting function
# Difficulty: Intermediate
def welcomer(time, name):
    cname = name.title()
    utime = time.upper()
    if utime.endswith("PM"):
        ctime = int(utime.replace("PM", " ").strip())
    else:
        ctime = int(utime.replace("AM", " ").strip())
    if ctime < 5 or ctime >= 11:
        time = "afternoon"
    elif time.endswith("PM"):
        time = "evening"
    else:
        time = "morning"
    print(f"Good {time}, {cname}!")

print("Input time:", end=" ")
time = input()

print("Input name:", end=" ")
name = input()

welcomer(time, name)