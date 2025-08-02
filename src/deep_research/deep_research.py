import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str, email: str = ""):
    async for chunk in ResearchManager().run(query, email):
        yield chunk


with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="neutral",
        secondary_hue="gray",
        neutral_hue="stone",
    ).set(
        body_background_fill="#0f1419",
        block_background_fill="transparent",
        block_border_color="transparent",
        input_background_fill="#2d3748",
        input_border_color="rgba(255,255,255,0.1)",
        button_primary_background_fill="#10a37f",
        button_primary_text_color="#ffffff",
    ),
    css="""
    .gradio-container {
        background: #0f1419 !important;
        color: #ffffff !important;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        padding: 2rem;
    }
    
    .main-panel {
        max-width: 768px;
        width: 100%;
        margin: 0 auto;
    }
    
    .app-title {
        color: #ffffff !important;
        text-align: center;
        font-size: 2rem !important;
        font-weight: 600 !important;
        margin-bottom: 3rem !important;
        letter-spacing: -0.025em;
    }
    
    .input-group {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .chat-input {
        background: #40414f !important;
        border: 1px solid rgba(86, 88, 105, 0.5) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        color: #ffffff !important;
        transition: all 0.2s ease !important;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1) !important;
    }
    
    .chat-input:focus {
        border-color: rgba(86, 88, 105, 0.8) !important;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1), 0 0 0 1px rgba(86, 88, 105, 0.3) !important;
        outline: none !important;
    }
    
    .chat-input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    .send-button {
        background: linear-gradient(180deg, #10a37f 0%, #0d8c6c 100%) !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        margin: 0 auto !important;
        display: block !important;
        min-width: 120px !important;
    }
    
    .send-button:hover {
        background: linear-gradient(180deg, #0d8c6c 0%, #0a7759 100%) !important;
        box-shadow: 0 2px 8px rgba(16, 163, 127, 0.3) !important;
    }
    
    .send-button:active {
        transform: translateY(1px) !important;
    }
    
    .results-area {
        background: transparent !important;
        border: none !important;
        padding: 2rem 0 !important;
        margin-top: 2rem !important;
        border-top: 1px solid rgba(86, 88, 105, 0.3) !important;
    }
    
    .results-area .markdown {
        color: #ffffff !important;
        line-height: 1.6 !important;
    }
    
    /* Remove Gradio's default styling */
    .gr-group {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    
    .gr-form {
        background: transparent !important;
        border: none !important;
    }
    
    .gr-panel {
        background: transparent !important;
        border: none !important;
    }
    
    .gr-box {
        background: transparent !important;
        border: none !important;
    }
    """
) as ui:
    with gr.Column(elem_classes="main-panel"):
        gr.HTML('<h1 class="app-title">Deep Research</h1>')
        
        with gr.Column(elem_classes="input-group"):
            query_textbox = gr.Textbox(
                label="Research Query",
                placeholder="What would you like me to research?",
                lines=2,
                elem_classes="chat-input"
            )
            email_textbox = gr.Textbox(
                label="Email (Optional)",
                placeholder="your@email.com",
                elem_classes="chat-input"
            )
            
        run_button = gr.Button(
            "Start Research",
            variant="primary",
            elem_classes="send-button"
        )
        
        with gr.Column(elem_classes="results-area"):
            report = gr.Markdown(
                "Enter your research query above and I'll analyze multiple sources to provide comprehensive insights.",
                label="Results"
            )
    
    run_button.click(fn=run, inputs=[query_textbox, email_textbox], outputs=report)
    query_textbox.submit(fn=run, inputs=[query_textbox, email_textbox], outputs=report)

ui.launch(inbrowser=True)

