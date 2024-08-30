from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-tYwyVNxsdhydCK176xm7m6XW", 
  model="gpt-3.5-turbo"
)