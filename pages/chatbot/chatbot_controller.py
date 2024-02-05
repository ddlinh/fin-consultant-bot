from dash.dependencies import Input, Output, State
from app import app

from components.textbox import render_textbox
from .chatbot_model import conversation

@app.callback(
    Output(component_id="display-conversation", component_property="children"),
    Input(component_id="store-conversation", component_property="data")
)
def update_display(chat_history):
    return [
        render_textbox(x, box="human") if i%2 == 0 else render_textbox(x, box="AI")
        for i, x in enumerate(chat_history.split("<split>")[:-1])
    ]

@app.callback(
    Output(component_id="user-input", component_property="value"),
    Input(component_id="submit", component_property="n_clicks"),
    Input(component_id="user-input", component_property="n_submit")
)
def clear_input(n_clicks, n_submit):
    return ""


@app.callback(
    Output(component_id="store-conversation", component_property="data"),
    Output(component_id="loading-component", component_property="children"),
    Input(component_id="submit", component_property="n_clicks"),
    Input(component_id="user-input", component_property="n_submit"),
    State(component_id="user-input", component_property="value"),
    State(component_id="store-conversation", component_property="data"),
)
def run_chatbot(n_clicks, n_submit, user_input, chat_history):
    if n_clicks == 0 and n_submit is None:
        return "", None

    if user_input is None or user_input == "":
        return chat_history, None

    chat_history += f"Human: {user_input}<split>ChatBot: "
    result_ai = conversation.predict(input=user_input)
    model_output = result_ai.strip()
    chat_history += f"{model_output}<split>"
    return chat_history, None