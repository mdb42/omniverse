"""Callback Handler streams to the response browser on new llm token."""

import sys
from typing import Any, Dict, List, Union

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult



class StreamingBrowserCallbackHandler(BaseCallbackHandler):
    """Callback handler for streaming. Only works with LLMs that support streaming."""

    def __init__(self, browser, parent=None):
        self.browser = browser
        self.received_non_newline = False

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any

    ) -> None:
       # print("LLM Started")
        """Run when LLM starts running."""

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        # print(token)
        if token == "\n\n" and not self.received_non_newline:
            print("New Line")
        else:
            self.received_non_newline = True
            self.browser.insertPlainText(token)
            self.browser.update()
            self.browser.repaint()
            self.browser.ensureCursorVisible()


    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        # print("LLM Ended")
        """Run when LLM ends running."""

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        print("LLM Error: " + str(error))
        """Run when LLM errors."""

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        print("Chain Started")
        """Run when chain starts running."""

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        print("Chain Ended")
        """Run when chain ends running."""

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        print("Chain Error")
        """Run when chain errors."""

    def on_tool_start(
        self, serialized: Dict[str, Any], action: AgentAction, **kwargs: Any
    ) -> None:
        print("Tool Started")
        """Run when tool starts running."""

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Run on agent action."""
        print("Agent Action")
        pass

    def on_tool_end(self, output: str, **kwargs: Any) -> None:
        print("Tool Ended")
        """Run when tool ends running."""

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        print("Tool Error")
        """Run when tool errors."""

    def on_text(self, text: str, **kwargs: Any) -> None:
        print("Text")
        self.browser("Text")
        """Run on arbitrary text."""

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> None:
        print("Agent Finished")
        """Run on agent end."""
