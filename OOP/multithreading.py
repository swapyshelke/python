import threading
import time

def walk_dog():
    time.sleep(8)
    print("Walking the dog")

def throw_trash():
    time.sleep(2)
    print("throwing trash")

def get_mail():
    time.sleep(4)
    print("getting the mail")

# walk_dog()
# throw_trash()
# get_mail()

chore1 = threading.Thread(target = walk_dog)
chore1.start()

chore2 = threading.Thread(target = throw_trash)
chore1.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all chores compelted")