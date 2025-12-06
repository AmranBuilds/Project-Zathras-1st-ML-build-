# Import the libraries
from openai import OpenAI
import time

# Connect to local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

print("🤖 Connecting to Local AI...")

# Start the timer
start_time = time.time()

# Send the message
response = client.chat.completions.create(
  model="model-identifier",
  messages=[
    {"role": "user", "content": "Write a science fiction story about a space pirate named Zathras. The story should be at least 300 words long."}
  ],
  temperature=0.7,
)

# Calculate the speed
speed = response.usage.completion_tokens / (time.time() - start_time)

# Print the answer to the screen
print("\n📝 AI Answer:")
print(response.choices[0].message.content)
print(f"\n⚡ Speed: {speed:.2f} tokens/sec")

# --- NEW PART: Save to a file ---
filename = "zathras_story.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(response.choices[0].message.content)

print(f"\n💾 SUCCESS: Story saved to '{filename}'")