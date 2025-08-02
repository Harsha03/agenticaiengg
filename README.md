# Agentic AI Engineering Project

👋 Hi, I'm Harsha Jaiganesh

🤖 Agentic AI Engineer & Multi-Agent Systems Specialist

Welcome to my laboratory for building autonomous AI agents that think, plan, and execute complex tasks! This repository showcases cutting-edge agentic AI implementations where multiple specialized agents collaborate to solve real-world problems. 🚀

From personal AI assistants that represent your professional identity to multi-agent research systems that autonomously gather and synthesize information, these projects demonstrate the future of AI: systems that don't just respond, but actively plan, search, analyze, and deliver results.

---

## 🚀 app.py
**Purpose:** Personal AI assistant and portfolio chatbot that represents Harsha Jaiganesh's professional profile through an intelligent conversational interface.

**Features:**
- **Personal AI Agent**: Creates an AI representation using OpenAI's GPT-4o-mini that can answer questions about Harsha's background, skills, and experience
- **Document Processing**: Automatically ingests and processes personal documents from the 'me' folder:
  - `linkedin.pdf`: LinkedIn profile extraction using PyPDF for comprehensive career information
  - `summary.txt`: Professional summary with detailed background in AI Engineering and Systems Engineering
- **Interactive Web Interface**: Gradio-powered chat interface for real-time conversations with the AI assistant
- **Lead Generation Tools**: Built-in function calling capabilities to:
  - Record user contact details when visitors express interest
  - Log unknown questions for continuous improvement
- **Notification System**: Pushover integration for real-time alerts when users interact or ask questions
- **Tool Integration**: OpenAI function calling for structured data collection and user engagement tracking
- **Professional Representation**: AI maintains character consistency as Harsha, steering conversations toward professional networking and contact collection

**Use Case:** Demonstrates advanced agentic AI implementation for personal branding and professional networking. Shows practical application of LLM function calling, document processing, and conversational AI for portfolio websites and professional representation.

**Technical Stack:** Python, OpenAI API, Gradio, PyPDF, Pushover API, dotenv for secure credential management

---

## 🚀 deep_research
**Purpose:** Autonomous multi-agent research system that conducts comprehensive web research and generates detailed reports with optional email delivery.

**Features:**
- **Multi-Agent Architecture**: Coordinated system of specialized AI agents working together:
  - `planner_agent.py`: Strategic planning agent that analyzes queries and creates optimal search strategies (generates 5 targeted web searches)
  - `search_agent.py`: Web research specialist that performs searches and creates concise 2-3 paragraph summaries (300 words max)
  - `writer_agent.py`: Senior researcher that synthesizes findings into comprehensive 5-10 page markdown reports (1000+ words)
  - `email_agent.py`: Communication agent that formats and sends HTML email reports via SendGrid
- **Intelligent Search Planning**: Breaks down complex queries into strategic web searches with reasoning
- **Asynchronous Processing**: Concurrent search execution for optimal performance and speed
- **Professional Web Interface**: Custom-styled Gradio interface with dark theme and ChatGPT-inspired design
- **Comprehensive Reporting**: Generates detailed markdown reports with summaries and follow-up questions
- **Email Integration**: Automatic HTML email delivery with professional formatting via SendGrid API
- **Real-time Streaming**: Live status updates throughout the research process
- **Error Handling**: Robust exception handling for failed searches and continued processing

**Use Case:** Demonstrates advanced agentic AI workflows for automated research and content generation. Perfect for market research, competitive analysis, academic research, and business intelligence gathering. Shows practical implementation of multi-agent coordination, web scraping, and automated report generation.

**Technical Stack:** Python, OpenAI API (GPT-4o-mini), Gradio, SendGrid API, Pydantic for data validation, asyncio for concurrent processing, custom agents framework

---