import streamlit as st
import io
import logging
from contextlib import redirect_stdout
from main import initialize, graph  # Make sure these are defined in main.py

# ---- Streamlit Page Setup ----
st.set_page_config(page_title="Deep Research AI", layout="wide")
st.title("🧠 Deep Research Agentic-AI System")

# ---- Logging Setup ----
log_stream = io.StringIO()
handler = logging.StreamHandler(log_stream)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
if handler not in logger.handlers:
    logger.addHandler(handler)

# ---- Initialize Session State ----
if "chat_state" not in st.session_state:
    st.session_state.chat_state = initialize("")  # Your initial LangGraph state
    st.session_state.messages = []
    st.session_state.cli_logs = []

# ---- Layout Setup ----
col_chat, col_logs = st.columns([4, 2])

# ---- Chat Column ----
with col_chat:
    st.subheader("💬 Research Chat")
    
    # Chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        elif msg["role"] == "assistant":
            st.chat_message("assistant").write(msg["content"])
    
    # Enhanced answer display - always show the latest if available
    if st.session_state.chat_state.get("enhanced"):
        st.subheader("Final Enhanced Answer:")
        st.write(st.session_state.chat_state["enhanced"])
    
    # Chat input
    user_input = st.chat_input("Ask or continue your research...")

    if user_input:
        # Display user message
        st.chat_message("user").write(user_input)
        
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Update the chat state for the graph
        if not st.session_state.chat_state.get("query"):
            st.session_state.chat_state["query"] = user_input  # Main query
        else:
            st.session_state.chat_state["followup_needed"] = True
            st.session_state.chat_state["followup_query"] = user_input

        # Process through LangGraph
        with st.spinner("Processing..."):
            stdout_buffer = io.StringIO()
            
            # Redirect stdout to capture CLI-like output
            with redirect_stdout(stdout_buffer):
                result = graph.invoke(st.session_state.chat_state)
            
            # Store the raw CLI output
            cli_output = stdout_buffer.getvalue()
            st.session_state.cli_logs.append(cli_output)
            
            # Update state with graph result
            st.session_state.chat_state.update(result)
            
            # Add response to messages
            if result.get("enhanced"):
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result["enhanced"]
                })
                st.chat_message("assistant").write(result["enhanced"])
            elif result.get("draft"):
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result["draft"]
                })
                st.chat_message("assistant").write(result["draft"])
            elif result.get("followup_query"):
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"I need more information: {result['followup_query']}"
                })
                st.chat_message("assistant").write(f"I need more information: {result['followup_query']}")

# ---- Logs Column ----
with col_logs:
    st.subheader("🪵Agent Logs")
    
    # Display the raw CLI output
    if st.session_state.cli_logs:
        st.text_area("Latest Agent Log", st.session_state.cli_logs[-1], height=500)
    else:
        st.text("No logs yet. Ask a question to see the agent's thinking process.")
    
    st.subheader("📚 Message History")
    for i, msg in enumerate(st.session_state.messages):
        with st.expander(f"Message {i+1} ({msg['role']})", expanded=False):
            st.write(msg["content"])

    st.subheader("🔧 Session State")
    st.json(st.session_state.chat_state)