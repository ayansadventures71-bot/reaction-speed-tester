import time
import random

print("Reaction Speed Test")
print("Wait for 'CLICK NOW!' then press Enter as fast as you can.")
input("Press Enter to start...")

#random delay between 2–5 seconds
delay = random.uniform(2, 5)
time.sleep(delay)

print("CLICK NOW!")

start_time = time.time()

input()  #wait for user to press enter

end_time = time.time()

reaction_time = end_time - start_time

print("Your reaction time:", round(reaction_time, 3), "seconds")

if reaction_time < 0.25:
    print("⚡ Lightning fast!")
elif reaction_time < 0.4:
    print("👍 Pretty good!")
else:
    print("😅 Try again!")