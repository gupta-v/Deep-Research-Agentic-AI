# 🧠 Deep Research Agentic-AI System

A sophisticated, multi-agent Agentic-AI system engineered for comprehensive research, rigorous analysis, and polished response generation for complex scholarly inquiries. This advanced system leverages LangGraph's orchestration capabilities to coordinate specialized AI agents in a meticulously designed sequential workflow, delivering thoroughly researched, authoritative answers with transparent reasoning processes and full visibility into each agent's decision-making path.

The system combines specialized research capabilities across multiple knowledge domains with advanced information synthesis and content refinement, ensuring responses that are not only comprehensive but also well-structured, contextually relevant, and tailored to each unique research query's specific requirements.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Command Line Interface](#command-line-interface)
  - [Streamlit Web Interface](#streamlit-web-interface)
- [How It Works](#how-it-works)
- [Customization](#customization)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

## Project Overview

The Deep Research Agentic-AI represents a cutting-edge research assistant meticulously architected using LangChain's modular framework, LangGraph's sophisticated agent orchestration, and LangSmith's comprehensive tracing capabilities.
Powered by Groq's high-performance inference engines, this system harnesses multiple specialized large language models to deliver exceptionally thorough, nuanced responses to complex research inquiries across diverse knowledge domains.

The system operates through an intelligently coordinated workflow of purpose-built specialist agents:

1. **Researcher Agent** - Conducts exhaustive information gathering across authoritative sources (Wikipedia, arXiv, Google Scholar, Tavily) with contextual awareness to construct a comprehensive knowledge foundation tailored to each specific query's requirements and domain context.

2. **Drafter Agent** - Employs advanced synthesis algorithms to transform raw research into cohesive, structured content through a recursive feedback mechanism that critically evaluates information completeness, identifies knowledge gaps, and adaptively requests targeted additional research when necessary.

3. **Enhancer Agent** - Applies sophisticated linguistic refinement, factual validation, and structural optimization to transform draft content into publication-quality responses with meticulous attention to accuracy, clarity, coherence, and presentation excellence.

This specialized agent decomposition a significant advancement over monolithic single-agent approaches—enables superior performance through dedicated expertise at each stage of the research process. The architecture provides unparalleled transparency by exposing each agent's reasoning chains, information evaluation criteria, and decision pathways throughout the research lifecycle.

## Features

- **Multi-Agent Workflow** - Coordinated specialists for research, drafting, and enhancement working in concert to produce superior results
- **Multiple Research Sources** - Integrates knowledge from Wikipedia, Google Scholar, arXiv, and Tavily web search for comprehensive coverage
- **Transparent Reasoning** - Visible agent logs reveal the system's thinking process, sources consulted, and decision-making rationale
- **Interactive Refinement** - Generates targeted follow-up questions when more information is needed to address specific knowledge gaps
- **State Management** - Maintains conversation context with LangGraph's state management for coherent multi-turn interactions
- **Streamlit Interface** - User-friendly web application with real-time agent activity monitoring showing each step of the research process
- **LangSmith Integration** - Complete tracing and monitoring capabilities for debugging and performance optimization

## Technology Stack

- **Core Frameworks**:

  - [LangChain](https://python.langchain.com/docs/introduction/) - For agent construction and tool integration, providing a flexible framework for building complex AI systems
  - [LangGraph](https://langchain-ai.github.io/langgraph/) - For building the agent workflow and state management, enabling sophisticated agent coordination
  - [LangSmith](https://docs.smith.langchain.com/) - For monitoring the agents, tools and state management with comprehensive tracing capabilities
  - [Streamlit](https://streamlit.io/) - For the web user interface with real-time visualization of agent activities

- **Language Models**:

  - [Groq](https://groq.com/) - Primary LLM provider for all agents, selected for its optimal balance of performance and cost
  - Models Used:
    - `meta-llama/llama-4-scout-17b-16e-instruct` - Optimized for research tasks with strong reasoning capabilities
    - `deepseek-r1-distill-llama-70b` - Selected for content synthesis and drafting with excellent writing abilities
    - `llama-3.3-70b-versatile` - Chosen for final content enhancement with superior language quality

- **Research Tools**:

  - Wikipedia API - For general knowledge lookup providing contextual background information
  - arXiv API - For scientific paper research accessing the latest academic publications
  - Google Scholar - For academic citations and papers with comprehensive scholarly coverage
  - Tavily - For web search capabilities delivering current and diverse information sources

- **Dependencies**:
  - `langchain` - Core agent and workflow framework
  - `langchain-groq` - Groq language model integration
  - `langchain-community` - Community-contributed tools and components
  - `langchain-core` - Essential LangChain interfaces and classes
  - `langchain-tavily` - Tavily search integration
  - `langsmith` - Tracing and monitoring framework
  - `langgraph` - Agent orchestration and state management
  - `typing-extensions` - Enhanced type annotations
  - `pydantic` - Data validation and settings management
  - `arxiv` - arXiv paper search and metadata retrieval
  - `google-search-results` - Google Scholar integration via SerpAPI
  - `wikipedia` - Wikipedia knowledge access
  - `streamlit` - Interactive web interface

## System Architecture

The system is built on a LangGraph workflow with three main components working together in a coordinated process:

```
Query → [Researcher] → [Drafter] → (Needs more info? Back to Researcher) → [Enhancer] → Final Answer
```

- **LangGraph State Flow** - Coordinates agent activities and communication through a well-defined state machine
- **LangChain Tools** - Integrates external knowledge sources through structured tools with consistent interfaces
- **LangSmith Monitoring** - Enables LangSmith tracing to track and monitor the workflow with all integrated tools and states
- **Groq AI Models** - Powers the system with specialized language models for different tasks, each optimized for its specific role

## File Structure

```
Deep-Research-Agentic-AI/
│
├── main.py                         # 🚀 Entry point to run the graph/ CLI inference
├── app.py                          # 📱 Streamlit application
│
├── state/
│   └── context.py                  # 🧠 Shared state (TypedDict)
│
├── graph/
│   ├── graph_builder.py            # 🌐 LangGraph builder (node flow)
│   └── nodes.py                    # 🧩 All LangGraph node functions
│
├── agents/
│   ├── researcher.py               # 🔍 Research agent (LLM + tools)
│   ├── drafter.py                  # ✍️ Drafting agent (LLM w/feedback loop)
│   └── enhancer.py                 # 🧼 Final enhancer/validator (LLM)
│
├── tools/                          # 🔧 Custom tools wrapped for LangChain
│   ├── wikipedia.py                # 📚 Wikipedia knowledge tool
│   ├── arxiv.py                    # 📑 arXiv research paper tool
│   ├── scholar.py                  # 🎓 Google Scholar citation tool
│   └── tavily.py                   # 🔎 Tavily web search tool
│
|
├── requirements.txt                # 📦 All dependencies
├── .env                            # 🔐 API keys and secrets
├── .env.example                    # 📄 Example environment variables template
├── .gitignore                      # 🚫 Files to ignore in git
└── README.md                       # 📚 Documentation for the project
```

## Getting Started

### Prerequisites

- [VS Code IDE](https://code.visualstudio.com/) - Recommended for optimal development experience with Python and virtual environment integration
- [Python 3.10+](https://www.python.org/downloads/) - Required for compatibility with all dependencies
- [LangSmith API key](https://smith.langchain.com/) - For tracing and monitoring agent workflows
- [Groq API key](https://console.groq.com/keys) - For accessing the language models
- [SERP API key](https://serpapi.com/) - For Google Scholar integration
- [Tavily API key](https://app.tavily.com/) - For web search capabilities

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Deep-Research-Agentic-AI.git
   cd Deep-Research-Agentic-AI
   ```

2. Create and activate a virtual environment:

   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create your environment variables file:

   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit the .env file with your API keys
   ```

5. Open the `.env` file and add your API keys here:
   ```
   GROQ_API_KEY="your_groq_api_key"
   TAVILY_API_KEY="your_tavily_api_key"
   SERP_API_KEY="your_google_scholar_api_key"
   LANGSMITH_API_KEY="your_langsmith_project_api_key"
   LANGSMITH_PROJECT="your_project_name"   specify the project name
   ```

### Configuration

The system uses different AI models for different agents. You can customize these in the respective agent files:

- `researcher.py` - Uses `meta-llama/llama-4-scout-17b-16e-instruct` by default for optimal research capabilities
- `drafter.py` - Uses `deepseek-r1-distill-llama-70b` by default for high-quality content drafting
- `enhancer.py` - Uses `llama-3.3-70b-versatile` by default for superior content enhancement

Each agent can be configured with different parameters:

- Temperature settings - Adjust creativity vs determinism
- Context window size - Balance between history retention and speed
- Tool selection - Enable or disable specific research tools
- Response formats - Customize output structure for specific needs

## Usage

### Command Line Interface

Run the system from the command line:

```bash
python main.py
```

You'll be prompted to enter your research query. The system will then:

1. Research your query across multiple sources with the Researcher agent
2. Draft an initial answer based on research findings with the Drafter agent
3. Enhance the draft into a polished, well-structured response with the Enhancer agent

The CLI interface shows real-time updates on each agent's progress and thinking process.

### Streamlit Web Interface

For a more user-friendly experience, launch the Streamlit app:

```bash
streamlit run app.py
```

This provides:

- Chat interface for queries and follow-ups with a clean message history
- Real-time agent logs showing the system's thought process and tool usage
- State visualization to track the flow of information between agents
- Ability to ask follow-up questions that build on previous context
- Options to customize research parameters for specific needs

Example queries to try:

- "What are the latest advances in large language model training techniques?"
- "How does quantum computing differ from classical computing?"
- "Summarize recent research on climate change mitigation strategies"

## How It Works

1. **Query Processing**: Your query is analyzed to determine research requirements and knowledge domains
2. **Research Phase**: The Researcher agent gathers information from Wikipedia, arXiv, Google Scholar, and web search
   - Identifies key concepts and relationships in the query
   - Selects appropriate research tools based on the query domain
   - Retrieves relevant information from multiple sources
   - Organizes findings into a structured research summary
3. **Draft Creation**: The Drafter agent analyzes research context and creates a coherent draft
   - Synthesizes information from all research sources
   - Structures content logically with clear sections
   - Identifies potential information gaps
   - If information is insufficient, it will request specific follow-up questions
4. **Enhancement**: The Enhancer agent improves the draft for clarity, structure, and accuracy
   - Refines language for precision and readability
   - Ensures logical flow and coherent structure
   - Verifies factual accuracy against research findings
   - Adds appropriate formatting and organization
5. **Final Answer**: The system returns a comprehensive, well-formed response with clear attribution to sources

The system maintains state between interactions, allowing for follow-up questions that build on previous context and research history.

## Customization

### Adding New Research Tools

Add new tools to the `tools/` directory following the pattern of existing tools:

1. Create a new file like `my_tool.py`
2. Implement your tool using LangChain's tool framework:

   ```python
      from langchain.tools import BaseToolAPIWrapper
      from langchain_core.tools import Tool

      # --- Tool Setup ---                             # Check documentation of tools to configure the tool
      base_tool_api = BaseToolAPIWrapper(
         parameter1=x,
         parameter2=y,
         parameter3=z,
      )

      def base_tool_search(query: str) -> str:
         return base_tool_api.run(query)

      myNewTool = Tool(                               # Check documentation of tools to configure the tool
         name="Base Tool Search",
         func=base_tool_search,
         description="Search the results from Base Tool"
      )

   ```

3. Import and add your tool to the list in `researcher.py`:

   ```python
   from tools.my_tool import myNewTool

   # In the tools list
   tools = [wikipedia, arxiv, scholar, tavily, myNewTool, ] # Add your new tool here
   ```

## Future Enhancements

- **Citation tracking and verification** - Implement a system to track and verify citations for academic credibility
- **Academic paper summarization** - Add specialized capabilities for condensing complex research papers
- **PDF document analysis** - Enable direct analysis of uploaded PDF documents
- **Local document search** - Add capability to search through user-provided document collections
- **User preference memory** - Store and apply user preferences for research style and detail level
- **Multiple LLM provider support** - Expand beyond Groq to support other LLM providers
- **Cross-language research** - Enhance capabilities to research in multiple languages
- **Interactive visualization** - Add data visualization tools for research findings
- **Audio and video source analysis** - Expand beyond text to include multi-modal research
- **Collaborative research sessions** - Enable multiple users to contribute to a shared research project

## Acknowledgments

- Built with:
  - [LangChain](https://python.langchain.com/docs/introduction/) - Providing the agent and tool framework
  - [LangGraph](https://langchain-ai.github.io/langgraph/) - Enabling sophisticated agent orchestration
  - [LangSmith](https://docs.smith.langchain.com/) - Supporting comprehensive workflow tracing
- Powered by [Groq](https://groq.com/) language models for high-performance inference
- Research tools: Wikipedia, arXiv, Google Scholar, and Tavily
- Inspired by latest research in Agentic-AI systems and collaborative intelligence
