from datetime import datetime

import tiktoken
from langchain import PromptTemplate, OpenAI
from langchain.chat_models import ChatOpenAI

from src.llms.chains.dynamic_chain import DynamicChain
from src.llms.memory.dynamic_memory import DynamicMemory
from src.llms.prompts.protocol_templates import ASSISTANT_TEMPLATE
import src.data.data_utils as data_utils

class LLMManager:
    def __init__(self, *args, **kwargs):
        self.session = kwargs.get('session', None)
        self.browser_callbacks = kwargs.get('browser_callbacks', None)
        self.assistant_id = kwargs.get('assistant_id', None)
        self.system_id = "system"
        self.temperature = 0.1
        self.current_input = ""
        self.current_output = ""
        self.current_prompt = ""

        self.protocols = ["Assistant", "Tutor", "Storyteller", "Persona"]
        self.current_protocol = "Assistant"
        self.llm_models = ["gpt-3.5-turbo", "text-davinci-003"]
        self.current_llm_model = "gpt-3.5-turbo"

        self.current_summary = ""
        self.current_chat_history_string = ""
        self.current_entities = ""
        self.current_sentiment = ""
        self.current_knowledge = ""

        self.prompt_token_count = 0
        self.summary_token_count = 0
        self.output_token_count = 0
        self.total_token_count = 0

        self.sentiment_llm = None
        self.entity_llm = None
        self.knowledge_llm = None
        self.summary_llm = None
        self.memory = None

        self.session_template = ASSISTANT_TEMPLATE
        self.session_prompt = PromptTemplate(input_variables=["chat_lines", "summary", "sentiment_analysis", "input", "ai_name", "user_name"],
                                             template=self.session_template)

        self.chat_llm = None
        self.chat_chain = None
        self.davinci_llm = None
        self.davinci_chain = None
        # self.setup()
        print("LLM Manager: Initialized")

    def setup(self):
        print("LLM Manager: Setting Up LLMs")
        self.sentiment_llm = ChatOpenAI(streaming=True,
                                        callback_manager=self.browser_callbacks["sentiment"],
                                        verbose=True,
                                        temperature=0,
                                        openai_api_key=data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key))

        self.entity_llm = ChatOpenAI(streaming=True,
                                     callback_manager=self.browser_callbacks["entity"],
                                     verbose=True,
                                     temperature=0,
                                     openai_api_key=data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key))

        self.knowledge_llm = ChatOpenAI(streaming=True,
                                        callback_manager=self.browser_callbacks["knowledge"],
                                        verbose=True,
                                        temperature=0,
                                        openai_api_key=data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key))

        self.summary_llm = ChatOpenAI(streaming=True,
                                      callback_manager=self.browser_callbacks["summary"],
                                      verbose=True,
                                      temperature=0,
                                      openai_api_key=data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key))

        self.memory = DynamicMemory(summary_llm=self.summary_llm,
                                    entity_llm=self.entity_llm,
                                    knowledge_llm=self.knowledge_llm,
                                    sentiment_llm=self.sentiment_llm,
                                    verbose=False,
                                    session=self.session,
                                    ai_name=self.assistant_id)

        self.chat_llm = ChatOpenAI(streaming=True,
                                   callback_manager=self.browser_callbacks["response"],
                                   verbose=True,
                                   temperature=self.temperature,
                                   openai_api_key=data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key))
        
        self.chat_chain = DynamicChain(prompt=self.session_prompt,
                                       llm=self.chat_llm,
                                       verbose=False)

        self.davinci_llm = OpenAI(streaming=True,
                                  model_name="text-davinci-003",
                                  callback_manager=self.browser_callbacks["response"],
                                  verbose=True,
                                  temperature=self.temperature,
                                  openai_api_key=data_utils.decrypt(self.session.get_key_by_provider('OpenAI').key))

        self.davinci_chain = DynamicChain(prompt=self.session_prompt,
                                          llm=self.davinci_llm,
                                          verbose=False)
        
        self.set_protocol(self.current_protocol)

    def set_protocol(self, protocol: str):
        self.current_protocol = protocol
        self.chat_chain.set_protocol(self.current_protocol)
        self.davinci_chain.set_protocol(self.current_protocol)

    def preprocessing(self, current_input: str):
        print("LLM Manager Preprocessing")
        self.current_input = current_input
        self.memory.preprocessing(self.current_input)
        self.current_sentiment = self.memory.current_sentiment
        self.current_entities = self.memory.current_entities

    def generate_response(self):
        print("LLM Manager: Generating Response")
        print("Input: " + self.current_input)
        if self.current_llm_model == "gpt-3.5-turbo":
            print("Running Chat Chain")
            self.current_output = self.chat_chain.run(input=self.current_input,
                                                      ai_name=self.assistant_id,
                                                      user_name=self.session.current_user.display_name,
                                                      chat_lines=self.current_chat_history_string,
                                                      sentiment_analysis=self.current_sentiment,
                                                      summary=self.current_summary)
            print("Chat Chain Output: " + self.current_output)
        elif self.current_llm_model == "text-davinci-003":
            print("Running Davinci Chain")
            self.current_output = self.davinci_chain.run(input=self.current_input,
                                                         ai_name=self.assistant_id,
                                                         user_name=self.session.current_user.display_name,
                                                         chat_lines=self.current_chat_history_string,
                                                         sentiment_analysis=self.current_sentiment,
                                                         summary=self.current_summary)
            print("Davinci Chain Output: " + self.current_output)   

        print("Output: " + self.current_output)
        print("LLM Manager: Response Generated")
        return self.current_output

    def postprocessing(self, current_input: str, current_output: str):
        print("LLM Manager: Postprocessing")
        self.current_output = current_output
        self.current_input = current_input
        self.memory.current_output = self.current_output
        self.current_chat_history_string = self.memory.generate_new_chat_history()
        self.memory.postprocessing(self.current_input)
        self.current_summary = self.memory.current_summary
        self.current_knowledge = self.memory.current_knowledge
        self.memory.add_message("user", self.current_input, self.session.current_user.display_name, datetime.now())
        self.memory.add_message("assistant", self.current_output, self.assistant_id, datetime.now())

    def report_tokens(self):
        print("LLM Manager: Reporting Tokens")
        self.summary_token_count = self.get_token_count(self.current_summary)
        self.prompt_token_count = self.get_token_count(self.current_prompt)
        self.output_token_count = self.get_token_count(self.current_output)
        self.total_token_count = self.prompt_token_count + self.output_token_count
        print("Prompt Token Count: " + str(self.prompt_token_count))
        print("Summary Token Count: " + str(self.summary_token_count))
        print("Response Token Count: " + str(self.output_token_count))
        print("Total Token Count: " + str(self.total_token_count))

    def get_token_count(self, prompt: str) -> int:
        encoding_model = 'p50k_base'
        enc = tiktoken.get_encoding(encoding_model)
        tokens = enc.encode(prompt)
        return len(tokens)

    def set_model(self, model: str):
        self.current_llm_model = model

    def set_temperature(self, temperature: float):
        self.temperature = temperature
        self.setup()

