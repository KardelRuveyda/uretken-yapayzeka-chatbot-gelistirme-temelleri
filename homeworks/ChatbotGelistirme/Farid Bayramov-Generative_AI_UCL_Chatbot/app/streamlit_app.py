import streamlit as st
import datetime
from gpt_model import get_ai_response # Assuming this exists and works

st.set_page_config(page_title="Şampiyonlar Ligi Sohbeti", page_icon="⚽", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400;700&display=swap');
    
    /* Ensure html and body take full height and prevent main scroll */
    html, body,#root, .stApp, main  {
        height: 100%;
        margin: 0;
        overflow: hidden; /* Prevents main page scroll */
    }

    /* Main Streamlit App container - This is the parent flex container */
    .stApp {
        background-color: #0d1a2e;
        background-image: url("https://images.unsplash.com/photo-1541819777-a89a7f3f2d2b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGZufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        display: flex;
        flex-direction: column; /* Stack children vertically */
        height: 100vh; /* Full viewport height */
        padding: 0; /* No padding here, manage spacing with internal elements */
        box-sizing: border-box;
        overflow:hidden
    }
    
    /* Header Section: FIXED at the top */
    .stApp > header { /* Targets Streamlit's default header container */
        background-color: rgba(13, 26, 46, 0.9); 
        padding: 20px;
        box-sizing: border-box;
        flex-shrink: 0; /* Prevents header from shrinking */
        border-bottom: 1px solid #30475e;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    }

    h1 {
        font-family: 'Orbitron', sans-serif;
        color: #ffda00;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
        padding-bottom: 10px;
        border-bottom: 3px solid #ffda00;
        margin-bottom: 0px; 
        margin-top: 0px; 
    }
    
    .stMarkdown p {
        text-align: center;
        font-size: 1.1em;
        color: #c0c0c0;
        margin-top: 10px; 
        margin-bottom: 0px;
    }

    /* Wrapper for the chat box: Takes all remaining space, centers chat box */
    .chat-container-wrapper {
        flex-grow: 1; /* Takes all available space between header and fixed input */
        display: flex;
        justify-content: center; /* Center horizontally */
        align-items: center; /* Center vertically */
        padding: 20px; /* Padding around the fixed chat box */
        min-height: 0; /* Essential for flex item that's a container for scrollable content */
    }

    /* The actual chat box frame: This whole box is FIXED */
    .chat-container {
        background-color: rgba(17, 34, 51, 0.95);
        border-radius: 15px;
        padding: 0; /* No padding here, padding goes inside scrollable and input areas */
        max-width: 700px; /* Max width of the chat box */
        width: 100%; /* Take full width up to max-width */
        display: flex;
        flex-direction: column; /* Messages and input stack vertically */
        overflow: hidden; /* Crucial: Ensures content within doesn't spill out */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        border: 1px solid #30475e;
        height: 100%; /* Take full height of its parent (chat-container-wrapper) */
        max-height: 100%; /* Ensure it doesn't exceed parent height */
    }

    /* Message Area: THIS IS THE ONLY SCROLLABLE PART */
    .message-area {
        flex-grow: 1; /* Takes all available space for messages within chat-container */
        overflow-y: auto; /* Enable vertical scrolling ONLY for this area */
        padding: 15px; /* Padding for messages inside the scrollable area */
        display: flex;
        flex-direction: column;
        min-height: 0; /* Important for scrollable flex items */
    }

    /* Input Area: FIXED at the bottom of the chat box */
    .input-area-fixed {
        flex-shrink: 0; /* Prevents shrinking */
        padding: 15px;
        border-top: 1px solid #30475e;
        background-color: rgba(17, 34, 51, 0.95);
        border-radius: 0 0 15px 15px;
        display: flex; /* Use flex for input and button alignment */
        gap: 10px; /* Space between input and button */
        align-items: center; /* Vertically align items */
    }

    /* Custom styling for messages (existing) */
    .user-message {
        background-color: #2a3f5a;
        color: #ffffff;
        padding: 10px 15px;
        border-radius: 15px 15px 0 15px;
        margin-bottom: 10px;
        align-self: flex-end;
        max-width: 85%;
        word-wrap: break-word;
        font-size: 0.95em;
        box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }

    .bot-message {
        background-color: #1f2e3c;
        color: #e0e0e0;
        padding: 10px 15px;
        border-radius: 15px 15px 15px 0;
        margin-bottom: 10px;
        align-self: flex-start;
        max-width: 85%;
        word-wrap: break-word;
        font-size: 0.95em;
        box-shadow: -1px 1px 3px rgba(0, 0, 0, 0.2);
    }

    .message-timestamp {
        font-size: 0.7em;
        color: #909090;
        margin-top: 3px;
        text-align: right;
    }

    .bot-message .message-timestamp {
        text-align: left;
    }

    /* Streamlit input styling (existing) */
    .stTextInput > div > div > input {
        background-color: #1f2e3c;
        color: #e0e0e0;
        border: 1px solid #30475e;
        border-radius: 8px;
        padding: 10px 15px;
        font-size: 1em;
        width: 100%; 
    }

    .stTextInput > div > div > input:focus {
        border-color: #ffda00;
        box-shadow: 0 0 5px rgba(255, 218, 0, 0.5);
        outline: none;
    }

    .stButton button {
        background-color: #ffda00;
        color: #0d1a2e;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1em;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
        width: 100%;
        white-space: nowrap; 
    }

    .stButton button:hover {
        background-color: #ffe033;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("UEFA Champions League Chatbot ⚽")
st.markdown("<p>Ask anything you want to know about the Champions League!</p>", unsafe_allow_html=True)

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "processing_user_input" not in st.session_state:
    st.session_state.processing_user_input = None # Stores the input currently being processed by the bot

# --- Streamlit Layout Structure ---

st.markdown("<div class='chat-container-wrapper'>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

    # Message Area: THIS IS THE ONLY SCROLLABLE PART
    # We will use a placeholder here to dynamically update messages
    message_area_placeholder = st.empty() 

    # Input Area: This section contains the text input and send button
    st.markdown("<div class='input-area-fixed'>", unsafe_allow_html=True)
    input_col, button_col = st.columns([5, 1])

    with input_col:
        user_input_widget = st.text_input(
            "Type something...",
            key="user_input_widget",
            label_visibility="collapsed",
            on_change=lambda: handle_submit(st.session_state.user_input_widget)
        )

    with button_col:
        st.button("Send", on_click=lambda: handle_submit(st.session_state.user_input_widget))

    st.markdown("</div>", unsafe_allow_html=True) # Close input-area-fixed HTML div
    st.markdown("</div>", unsafe_allow_html=True) # Close chat-container HTML div

st.markdown("</div>", unsafe_allow_html=True) # Close chat-container-wrapper HTML div

# --- Helper function to render messages ---
def render_messages(placeholder, messages_list):
    with placeholder.container(): # Use a container within the placeholder
        st.markdown("<div class='message-area'>", unsafe_allow_html=True) # Re-add the message-area div
        for message in messages_list:
            if isinstance(message["time"], str):
                try:
                    message["time"] = datetime.datetime.fromisoformat(message["time"])
                except ValueError:
                    message["time"] = datetime.datetime.now()

            timestamp = message["time"].strftime("%H:%M")
            
            if message["role"] == "user":
                st.markdown(f"""
                    <div style='display: flex; justify-content: flex-end;'>
                        <div class='user-message'>{message["content"]}
                            <div class='message-timestamp'>{timestamp}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else: # bot message
                st.markdown(f"""
                    <div style='display: flex; justify-content: flex-start;'>
                        <div class='bot-message'>{message["content"]}
                            <div class='message-timestamp'>{timestamp}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True) # Close message-area HTML div


# --- Callback Function for Input/Button ---
def handle_submit(user_input):
    if user_input:
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input, "time": datetime.datetime.now()})
        
        # Store the input to be processed and trigger bot response logic
        st.session_state.processing_user_input = user_input
        
        # Clear the input box immediately
        st.session_state.user_input_widget = ""
        
        # Manually trigger a rerun so the main script can pick up processing_user_input
        st.rerun()

# --- Main Logic for Displaying Messages and Handling Bot Response ---

# Always render existing messages first
render_messages(message_area_placeholder, st.session_state.messages)


# If there's user input waiting to be processed by the bot
if st.session_state.processing_user_input:
    current_user_input = st.session_state.processing_user_input
    
    # Temporarily append a "Typing..." message for immediate display
    st.session_state.messages.append({"role": "bot", "content": "Typing...", "time": datetime.datetime.now()})
    render_messages(message_area_placeholder, st.session_state.messages)

    # Call the AI model. This will block execution.
    bot_response = get_ai_response(current_user_input)

    # Replace "Typing..." with the actual bot response
    # Find and update the last bot message (which was "Typing...")
    # This assumes "Typing..." is always the last bot message when we're processing
    if st.session_state.messages and st.session_state.messages[-1]["content"] == "Typing...":
        st.session_state.messages[-1]["content"] = bot_response
    else: # Fallback if for some reason "Typing..." wasn't the last, just append
        st.session_state.messages.append({"role": "bot", "content": bot_response, "time": datetime.datetime.now()})

    # Clear the processing flag
    st.session_state.processing_user_input = None

    # Render all messages again to show the updated bot response
    render_messages(message_area_placeholder, st.session_state.messages)