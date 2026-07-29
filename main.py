import os
import time
from dotenv import load_dotenv
from rich import print
from rich.prompt import IntPrompt
from tqdm import tqdm
from google import genai
from mistralai.client import Mistral
from groq import Groq

load_dotenv("env.txt")

def show_menu():
    ans = IntPrompt.ask(r"""[dark_orange]
         (  )  (   )
        ) (   )  (
       (   ) (    )
      ____________
     /            \
    |  COFFEE HUB  |___
    |    v0.0.3    |   \
     \            /____/
      \__________/
       (________)

Select model:
1. gemini-2.5-flash (Google AI Studio)
2. mistral-large-latest (Mistral AI)
3. llama-3.3-70b-versatile (Groq Cloud)
""")
    return ans


while True:
    ans = show_menu()

    if ans == 1:
        print("Chat with gemini-2.5-flash (Google AI Studio) started. Type 'exit' to leave.")
        client = genai.Client()
        chat = client.chats.create(model="gemini-2.5-flash")

        while True:
            user_input = input("You:")
            if user_input.strip().lower() == "exit":
                break

            response = chat.send_message(user_input)
            print(f"Gemini: {response.text}")

            for i in tqdm(
                range(12),
                desc="Cooldown (limit 5 req/min)",
            ):
                time.sleep(1)

    elif ans == 2:
        print("Chat with mistral-large-latest (Mistral AI) started. Type 'exit' to leave.")
        client = Mistral()
        messages = []

        while True:
            user_input = input("You:")
            if user_input.strip().lower() == "exit":
                break

            messages.append({"role": "user", "content": user_input})

            response = client.chat.complete(
                model="mistral-large-latest",
                messages=messages
            )

            bot_reply = response.choices[0].message.content
            print(f"Mistral: {bot_reply}")
            messages.append({"role": "assistant", "content": bot_reply})

            for i in tqdm(
                range(2),
                desc="Cooldown (limit 30 req/min)",
            ):
                time.sleep(1)

    elif ans == 3:
        print("Chat with llama-3.3-70b-versatile (Groq Cloud) started. Type 'exit' to leave.")
        client = Groq()
        messages = []

        while True:
            user_input = input("You:")
            if user_input.strip().lower() == "exit":
                break

            messages.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )

            bot_reply = response.choices[0].message.content
            print(f"Groq (Llama): {bot_reply}")
            messages.append({"role": "assistant", "content": bot_reply})

            for i in tqdm(
                range(2),
                desc="Cooldown (limit 30 req/min)",
            ):
                time.sleep(1)
