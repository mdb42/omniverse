from typing import List, Dict, Any
from datetime import datetime

from langchain import BasePromptTemplate, LLMChain
from langchain.schema import BaseMemory
from langchain.base_language import BaseLanguageModel
from pydantic import BaseModel

from local import constants
from src.llms.prompts.memory_templates import SUMMARIZER_PROMPT, ENTITY_EXTRACTION_PROMPT, \
    KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT, SENTIMENT_ANALYSIS_PROMPT

import asyncio

class DynamicMemory(BaseMemory, BaseModel):
    """Memory class for storing information."""
    summary_llm: BaseLanguageModel
    entity_llm: BaseLanguageModel
    knowledge_llm: BaseLanguageModel
    sentiment_llm: BaseLanguageModel
    summarizer_prompt: BasePromptTemplate = SUMMARIZER_PROMPT
    entity_extraction_prompt: BasePromptTemplate = ENTITY_EXTRACTION_PROMPT
    knowledge_extraction_prompt: BasePromptTemplate = KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT
    sentiment_analysis_prompt: BasePromptTemplate = SENTIMENT_ANALYSIS_PROMPT


    session_messages: List = []
    message_buffer: List = []
    message_buffer_length: int = 10
    chat_history_string: str = ""
    current_knowledge: str = ""
    current_entities: str = ""
    current_sentiment: str = ""

    current_input: str = ""
    current_output: str = ""

    current_summary: str = ""
    previous_summary: str = ""

    memory_string: str = ""
    memory_key: str = "dynamic_memory"

    def clear(self):
        self.memory_string = ""
        self.current_summary = ""
        self.previous_summary = ""
        self.current_knowledge = ""
        self.current_entities = ""
        self.current_sentiment = ""
        self.current_input = ""
        self.current_output = ""
        self.session_messages = []
        self.message_buffer = []
        self.chat_history_string = ""

    @property
    def memory_variables(self) -> List[str]:
        """Define the variables we are providing to the prompt."""
        return [self.memory_key]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        return self.memory_string

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        """Save context from this conversation to buffer."""
        self.memory_string = self.generate_new_memory()

    def preprocessing(self, input):
        print("Preprocessing")
        self.current_input = input
        loop = asyncio.get_event_loop()
        try:
            self.current_sentiment, self.current_entities, server_info = loop.run_until_complete(asyncio.gather(
                self.generate_new_sentiment_analysis(),
                self.generate_new_entities(),
                self.get_server_info()
            ))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def postprocessing(self, input):
        print("Postprocessing")
        self.current_input = input
        loop = asyncio.get_event_loop()
        try:
            self.current_summary, self.current_knowledge, server_info = loop.run_until_complete(asyncio.gather(
                self.generate_new_summary(),
                self.generate_new_knowledge()
            ))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    async def generate_new_summary(self) -> str:
        print("Generating new summary")
        new_summary = "Default summary."
        summarizer_chain = LLMChain(llm=self.summary_llm, prompt=self.summarizer_prompt)
        if len(self.message_buffer) > 2:
            print("Last summary: ", self.current_summary)
            print("Last 4 messages: ", self.get_last_k_messages(4))
            new_summary = await summarizer_chain.arun(current_summary=self.current_summary, chat_history=self.get_last_k_messages(4))
        self.previous_summary = self.current_summary
        self.current_summary = new_summary
        return new_summary

    def generate_new_chat_history(self) -> str:
        print("Generating new chat history")
        new_chat_history = ""
        for message in self.message_buffer:
            speaker = message.get("speaker", "")
            content = message.get("content", "")
            if speaker and content:
                new_chat_history += f"{speaker.capitalize()}: {content}\n"
        self.chat_history_string = new_chat_history
        return new_chat_history

    async def generate_new_entities(self) -> str:
        print("Generating new entities")
        new_entities = "None"
        print("Running entity chain")
        chain = LLMChain(llm=self.entity_llm, prompt=self.entity_extraction_prompt)
        print("Entity chain created")
        if len(self.message_buffer) > 3:
            print("Last 4 messages: ", self.get_last_k_messages(4))
            print("Last message: ", self.current_input)
            new_entities = await chain.arun(history=self.get_last_k_messages(4), input=self.current_input)
            print("New entities: ", new_entities)
        return new_entities

    async def generate_new_sentiment_analysis(self) -> str:
        print("Generating new sentiment analysis")
        new_sentiment_analysis = "None"
        chain = LLMChain(llm=self.sentiment_llm, prompt=self.sentiment_analysis_prompt)
        if len(self.message_buffer) > 2:
            print("Last 3 messages: ", self.get_last_k_messages(3))
            print("Last message: ", self.current_input)
            new_sentiment_analysis = await chain.arun(history=self.get_last_k_messages(3), input=self.current_input)
            print("New sentiment analysis: ", new_sentiment_analysis)
        return new_sentiment_analysis

    async def generate_new_knowledge(self) -> str:
        print("Generating new knowledge triplets")
        new_knowledge = "None"
        chain = LLMChain(llm=self.knowledge_llm, prompt=self.knowledge_extraction_prompt)
        if len(self.message_buffer) > 1:
            print("Last 2 messages: ", self.get_last_k_messages(2))
            print("Last message: ", self.current_input)
            new_knowledge = await chain.arun(history=self.get_last_k_messages(2), input=self.current_input)
            print("New knowledge: ", new_knowledge)
        return new_knowledge

    def add_message(self, role: str, content: str, speaker: str, time: datetime) -> None:
        print("Adding message to buffer")
        message = {"role": role, "content": content, "speaker": speaker, "time": time}
        if len(self.message_buffer) > self.message_buffer_length:
            if self.message_buffer[0]["role"] == "system" and self.message_buffer[1]["role"] == "system":
                self.message_buffer.pop(0)
            if self.message_buffer[0]["role"] != "system":
                self.message_buffer.pop(0)
            else:
                self.message_buffer.pop(1)
        self.session_messages.append(message)
        self.message_buffer.append(message)
        print("Message added to buffer")

    def get_last_message(self) -> str:
        if len(self.session_messages) > 0:
            last_message = self.message_buffer[-1]
            return last_message["speaker"] + ": " + last_message["content"]
        else:
            return ""

    def get_last_k_messages(self, k: int) -> str:
        if len(self.session_messages) > 0:
            last_k_messages = self.session_messages[-k:]
            return "\n".join([message["speaker"] + ": " + message["content"] for message in last_k_messages])
        else:
            return ""



