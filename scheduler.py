import schedule
import time
import os
from app import run_one_episode

TOPICS = [
    "น้องมะขามหลงป่า",
    "น้องมะขามช่วยเพื่อนเก็บมะขาม",
    "น้องมะขามไปตลาดครั้งแรก",
    "น้องมะขามกลัวฟ้าร้อง",
    "น้องมะขามทำขนมให้เพื่อน",
]
day = 0
def job():
    global day
    topic = TOPICS[day % len(TOPICS)]
    day += 1
    print(f"ทำงาน EP: {topic}")
    run_one_episode(topic)

schedule.every().day.at("23:00").do(job)
print("ระบบถาวรเริ่มทำงานแล้ว")
job()
while True:
    schedule.run_pending()
    time.sleep(60)
