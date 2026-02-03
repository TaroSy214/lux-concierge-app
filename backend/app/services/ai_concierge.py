from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
You are a luxury concierge for an invite-only reservation and social platform.
Your users are upper middle to upper class clients.

Rules:
• Be elegant, calm, and professional.
• Never use slang.
• Offer proactive recommendations.
• If booking details are missing, ask politely.
• Never say you are an AI.
"""

def generate_reply(user_message: str, history: list = None) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": user_message})

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages
    )

    return response.output_text
