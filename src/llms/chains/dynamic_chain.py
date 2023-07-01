from langchain import PromptTemplate
from langchain.chains.llm import LLMChain

from src.llms.prompts.protocol_templates import ASSISTANT_TEMPLATE
from src.llms.prompts.protocol_templates import PERSONA_TEMPLATE
from src.llms.prompts.protocol_templates import SESSION_TEMPLATE
from src.llms.prompts.protocol_templates import STORYTELLER_TEMPLATE
from src.llms.prompts.protocol_templates import TUTOR_TEMPLATE


class DynamicChain(LLMChain):
    internal_chains: list = []
    internal_prompt: str = ''
    current_protocol: str = ''
    current_format: str = ''
    current_tone: str = ''
    messages: list = []
    template: str = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.internal_chains = []
        self.current_protocol = "Assistant"
        self.current_format = "Natural"
        self.current_tone = "Natural"

    def set_protocol(self, role):
        print("Setting chain role to "+role)
        self.current_protocol = role
        # print("Internal role: " +self.current_role)
        if self.current_protocol== "Assistant":
            self.template = ASSISTANT_TEMPLATE
        elif self.current_protocol== "Persona":
            self.template = PERSONA_TEMPLATE
        elif self.current_protocol== "Session":
            self.template = SESSION_TEMPLATE
        elif self.current_protocol== "Storyteller":
            self.template = STORYTELLER_TEMPLATE
        elif self.current_protocol== "Tutor":
            self.template = TUTOR_TEMPLATE
        self.prompt = PromptTemplate(input_variables=["chat_lines", "summary", "sentiment_analysis", "input", "ai_name", "user_name"],
                                           template=self.template)








