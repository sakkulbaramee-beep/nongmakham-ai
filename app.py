import os
import datetime
from openai import OpenAI
from anthropic import Anthropic

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

client_gpt = OpenAI(api_key=OPENAI_API_KEY)
client_claude = Anthropic(api_key=ANTHROPIC_API_KEY)

def step1_chatgpt(topic):
    res = client_gpt.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"ช่วยคิดบทซีรีส์น้องมะขาม เรื่อง: {topic} แบบสั้นๆ อบอุ่น น่ารัก มี 3 ฉาก"}]
    )
    return res.choices[0].message.content

def step2_claude(raw):
    res = client_claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1200,
        messages=[{"role": "user", "content": f"ช่วยเกลาบทนี้ให้น่ารักขึ้น ภาษาอบอุ่น เหมือนนิทานเด็ก: {raw}"}]
    )
    return res.text

def run_one_episode(topic):
    raw = step1_chatgpt(topic)
    final = step2_claude(raw)
    today = datetime.date.today().strftime("%Y-%m-%d")
    with open(f"บทน้องมะขาม_{today}.txt", "w", encoding="utf-8") as f:
        f.write(final)
    return final

if __name__ == "__main__":
    topic = os.environ.get("TODAY_TOPIC", "น้องมะขามหลงป่าแล้วเจอเพื่อนใหม่")
    run_one_episode(topic)
