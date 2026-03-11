
from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import re
import requests
from ollama import Client
from pypdf import PdfReader
import gradio as gr
client = Client(host='http://localhost:11434')

load_dotenv(override=True)
model_name = 'qwen3:8b'

def push(text):
    pushover_user = os.getenv("PUSHOVER_USER")
    pushover_token = os.getenv("PUSHOVER_TOKEN")
    pushover_url = "https://api.pushover.net/1/messages.json"
  
    requests.post(pushover_url, data={
        "token": pushover_token,
        "user": pushover_user,
        "message": text
    })

def record_user_details(email, name="Name not provider", notes ="No notes provided"):
    push(f"New user details:\nEmail: {email}\nName: {name}\nNotes: {notes}")
    return {"email": email,"recorder": "done"}

def record_unknown_question(question):
    push(f"Recording {question} asked by the user")
    return {"question": question,"recorder": "done"}

def should_record_email(user_message):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    has_email = re.search(email_pattern, user_message) is not None
    lowered = user_message.lower()
    wants_contact = any(phrase in lowered for phrase in [
        "contact me",
        "reach me",
        "get in touch",
        "email me",
        "call me",
        "connect with me"
    ])
    return has_email and wants_contact

def should_request_email(user_message):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    has_email = re.search(email_pattern, user_message) is not None
    lowered = user_message.lower()
    wants_contact = any(phrase in lowered for phrase in [
        "contact me",
        "reach me",
        "get in touch",
        "email me",
        "call me",
        "connect with me"
    ])
    return wants_contact and not has_email

def extract_email(user_message):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(email_pattern, user_message)
    return match.group(0) if match else ""



record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The email address of this user"
            },
            "name": {
                "type": "string",
                "description": "The user's name, if they provided it"
            }
            ,
            "notes": {
                "type": "string",
                "description": "Any additional information about the conversation that's worth recording to give context"
            }
        },
        "required": ["email"],
        "additionalProperties": False
    }
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question that couldn't be answered"
            },
        },
        "required": ["question"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": record_user_details_json},
        {"type": "function", "function": record_unknown_question_json}]

class Me:
        
    def __init__(self):
        val  = load_dotenv(override=True)
        self.name = "Abhishek Saxena"
        reader = PdfReader("me/linkedin.pdf")
        self.linkedin = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text
        with open("me/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()

    def handle_tool_calls(self, tool_calls):
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.get('function', {}).get('name', '')
            arguments = tool_call.get('function', {}).get('arguments', {})
            
            if isinstance(arguments, str):
                arguments = json.loads(arguments)
            
            print(f"Tool called: {tool_name}", flush=True)
            tool = globals().get(tool_name)
            result = tool(**arguments) if tool else {}
            
            results.append({
                "role": "tool",
                "content": json.dumps(result)
            })
        return results
    
    def system_prompt(self):

        system_prompt = f"""You are a helpful assistant that provides information about {self.name} based on the information provided in the LinkedIn Profile and Summary.\
        ## Summary \n {self.summary} \n \n ## LinkedIn Profile \n {self.linkedin}.\
        You have to assume character of {self.name} and reply as if you are {self.name}.\
        With this context, answer the question as best as you can.\
        Never say you are a language model or AI. Speak in first person as {self.name}.\
        If you do not know the answer, reply with exactly: I don't know.\
        If and only if your reply is exactly I don't know, call the record_unknown_question tool.\
        If the user provides an email address and wants to be contacted, \
        reply with exactly: Email is recorded and I will contact you soon.\
        If and only if your reply is exactly Email is recorded and I will contact you soon., call the record_user_details tool.\
        If the user asks to be contacted but did not provide an email, ask them to share their email address.\
        Never use the reply "Email is recorded and I will contact you soon." for greetings or when the user did not share an email and ask to be contacted.\
        For all other cases, reply normally and do not call any tool.\
        Chat with the user always staying in the character of an assistant poviding infomation about {self.name}.
        """
        return system_prompt
    
    def chat_with_me(self, message, chat_history):
        messages = [{"role": "system", "content": self.system_prompt()}] + chat_history + [
            {"role": "user", "content": message}
        ]
        done = False
        final_content = ""
        while not done:
            response = client.chat(
                model=model_name,
                messages=messages,
                tools=tools
            )
            
            # Check if there are tool calls
            tool_calls = response['message'].get('tool_calls') or []
            assistant_content = (response['message'].get('content') or "").strip()
            allowed_tool_calls = []

            if should_request_email(message):
                assistant_content = "Please share your email address so I can contact you."
                tool_calls = []
                allowed_tool_calls = []
                done = True
                final_content = assistant_content
                continue

            if assistant_content.lower() == "i don't know":
                allowed_tool_calls = [
                    call for call in tool_calls
                    if call.get("function", {}).get("name") == "record_unknown_question"
                ]
            elif assistant_content.lower() == "email is recorded and i will contact you soon.":
                if not should_record_email(message):
                    response = client.chat(
                        model=model_name,
                        messages=messages
                    )
                    assistant_content = (response['message'].get('content') or "").strip()
                    tool_calls = []
                else:
                    allowed_tool_calls = [
                        call for call in tool_calls
                        if call.get("function", {}).get("name") == "record_user_details"
                    ]
                    if not allowed_tool_calls:
                        email = extract_email(message)
                        if email:
                            print("Tool called: record_user_details", flush=True)
                            record_user_details(email=email)

            if not assistant_content and tool_calls and not allowed_tool_calls:
                # Retry without tools when the model returns only tool calls.
                response = client.chat(
                    model=model_name,
                    messages=messages
                )
                assistant_content = (response['message'].get('content') or "").strip()
                tool_calls = []
                allowed_tool_calls = []
            
            if allowed_tool_calls:
                # Add assistant message with tool calls to history
                messages.append(response['message'])
                # Handle tool calls and add results
                tool_results = self.handle_tool_calls(allowed_tool_calls)
                messages.extend(tool_results)
            else:
                final_content = assistant_content
                done = True
        
        return final_content

if __name__ == "__main__":
    me = Me()

    def gradio_history_to_messages(chat_history):
            """Normalize Gradio chat history into a list of message dicts:
            - Accepts chat_history as list of tuples [(user, bot), ...] (older style)
            - Or as list of message dicts [{'role':..., 'content':...}, ...] (new style)
            Returns list of dicts with 'role' and 'content'.
            """
            def normalize_content(content):
                if isinstance(content, list):
                    if content and isinstance(content[0], dict):
                        return str(content[0].get("text", ""))
                    return ""
                if isinstance(content, dict):
                    return str(content.get("text", ""))
                return str(content)

            messages = []
            if not chat_history:
                return messages
            # If history already in message-dict format
            if isinstance(chat_history, list) and len(chat_history) > 0 and isinstance(chat_history[0], dict):
                # assume it's already [{'role':..,'content':...}, ...]
                normalized = []
                for msg in chat_history:
                    if isinstance(msg, dict) and "role" in msg and "content" in msg:
                        normalized.append({
                            "role": msg["role"],
                            "content": normalize_content(msg["content"])
                        })
                return normalized

            # Otherwise assume list of pairs/tuples: (user_msg, bot_msg)
            for msg in chat_history:
                if isinstance(msg, dict):
                    # Handle dict format with role and content
                    if 'role' in msg and 'content' in msg:
                        content = normalize_content(msg["content"])
                        messages.append({"role": msg["role"], "content": content})
                elif isinstance(msg, (list, tuple)) and len(msg) >= 2:
                # Handle tuple format (user_msg, assistant_msg)
                    user_msg = msg[0]
                    assistant_msg = msg[1]
                    
                    # Extract text from user message
                    if isinstance(user_msg, dict):
                        user_msg = user_msg.get('text', str(user_msg))
                    messages.append({"role": "user", "content": normalize_content(user_msg)})
                    
                    # Extract text from assistant message
                    if assistant_msg:
                        if isinstance(assistant_msg, dict):
                            assistant_msg = assistant_msg.get('text', str(assistant_msg))
                        messages.append({"role": "assistant", "content": normalize_content(assistant_msg)})
            return messages

    def submit_fn(message, chat_history):
            # Normalize incoming chat_history into message dicts for the model
            history_msgs = gradio_history_to_messages(chat_history)
            reply = me.chat_with_me(message, history_msgs)
            # Build new history in messages format (list of dicts)
            new_history = history_msgs[:] if history_msgs else []
            new_history.append({"role": "user", "content": message})
            new_history.append({"role": "assistant", "content": reply})
            # Return the messages list (what this Chatbot version expects) and clear the textbox
            return new_history, ""

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        txt = gr.Textbox(placeholder="Enter your message here...")
        txt.submit(submit_fn, inputs = [txt, chatbot], outputs = [chatbot, txt])

    demo.launch()
        
        
    

