from langchain import PromptTemplate

SUMMARIZER_TEMPLATE = """Progressively summarize the lines of conversation provided, adding onto the current summary and returning a new summary. To construct the new summary, consider the text carefully, break it down into sections, identify the key points in each section, and compose an informative and accurate summary iterating these key points. If the current conversation involves a specific task, articulate that task clearly within the summary. If no chat history yet exists, just reply "This is the start of a new conversation." The new summary should preserve detail from the current summary so that anyone reading it could accurately recount the conversation from beginning to end.

EXAMPLE
Current Summary:
Matthew and Govinda greet each other, and Matthew requests advice about how to write a good summary. Govinda first defines a summary as a brief and concise overview of a text that faithfully captures the essence of a source without added information or opinion. Matthew asks how to start, and Govinda advises to read the source carefully, identify the main idea and supporting details, and to include relevant keywords or phrases. Govinda then explains to organize it into a logical structure and rewrite in his own words, avoiding copying sentences and instead paraphrasing or quoting, also using transition words and connectors to link sentences smoothly.

Chat History:
Matthew: Hello Govinda, I need help with writing a good summary. Can you give me some advice?

Govinda: Greetings, Matthew. A summary is a brief and concise overview of the main points of a text. It should capture the essence of the source without adding any new information or opinions.

Matthew: I see. So how do I start writing a summary?

Govinda: Well, first you need to read the source carefully and identify the main idea and supporting details. You should include keywords or phrases that are relevant to the topic.

Matthew: OK, then what?

Govinda: Then you need to organize it into a logical structure and write it in your own words. You should avoid copying sentences from the source and use paraphrasing or quoting techniques instead. You should also use transition words and connectors to link your sentences smoothly.

Matthew: How long should my summary be?

Govinda: Generally, a summary should be no more than 10% of the original length of the source.

New Summary:
Greeting each other, Matthew requests advice from Govinda about how to write a good summary. Govinda first defines a summary as a brief and concise overview of a text that faithfully captures the essence of a source without added information or opinion. Matthew asks how to start, and Govinda advises to read the source carefully, identify the main idea and supporting details, and to include relevant keywords or phrases. Govinda then explains to organize it into a logical structure and rewrite in his own words, avoiding copying sentences and instead paraphrasing or quoting, also using transition words and connectors to link sentences smoothly. Asked by Matthew how long a summary should be, Govinda recommends no more than 10% of the original source length.

END OF EXAMPLE

Current Summary:
{current_summary}

Chat History:
{chat_history}

New Summary: 
"""

SUMMARIZER_PROMPT = PromptTemplate(input_variables=["current_summary", "chat_history"],
                                           template=SUMMARIZER_TEMPLATE)

#######################################################################################################################
ENTITY_EXTRACTION_TEMPLATE = """You are reading the transcript of a conversation. Extract all of the proper nouns from the last message in the conversation. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.

The conversation history is provided just in case of a coreference (e.g. "What do you know about him" where "him" is defined in a previous line) -- ignore items mentioned there that are not in the last message.

Return the output as a single comma-separated list, or NONE if there is nothing of note to return (e.g. the user is just issuing a greeting or having a simple conversation).

EXAMPLE
Conversation history:
Alice: Hi Bob, how was your trip to Paris?
Bob: It was great! I visited the Eiffel Tower!
Alice: Nice! Did you get any pictures of it?
Last line:
Bob: Yes, I got many pictures of it.
Output: Alice, Bob, Eiffel Tower
END OF EXAMPLE

EXAMPLE
Conversation history:
John: "I ran into Bob and Tom at the store today!"
Sally: "Oh really? What did you talk about?"
John: "Oh we talked about their new horse, Samson."
Last line:
Sally: "Oh he's a great horse! They showed him to me last week."
Output: John, Sally, Bob, Tom, Samson
END OF EXAMPLE

Conversation history (for reference only):
{history}
Last line of conversation (for extraction):
{input}
Output:"""

ENTITY_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=ENTITY_EXTRACTION_TEMPLATE
)
#######################################################################################################################


KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE = (
    """Extract knowledge triples from the last two messages of conversation. A knowledge triple is a clause that contains a subject, a predicate, and an object. The subject is the entity being described, the predicate is the property of the subject that is being described, and the object is the value of the property. Generally, the subject for any triple will not be the speakers themselves, but rather the subject will be found within the content of their dialogue.
    
    EXAMPLE
    Conversation history:
    John: Did you hear aliens landed in Area 51?
    Susan: No, I didn't hear that. What do you know about Area 51?
    John: It's a secret military base in Nevada.
    Susan: What do you know about Nevada?
    Current Input:
    John: It's a state in the US. It's also the number 1 producer of gold in the US.
    
    Output: (Nevada, is a, state)<|>(Nevada, is in, US)<|>(Nevada, is the number 1 producer of, gold)
    END OF EXAMPLE
    
    EXAMPLE
    Conversation history:
    Jane: Hello.
    Adam: Hi! How are you?
    Jane: I'm good. How are you?
    Adam: I'm good too.
    Current Input:
    Jane: I'm going to the store.    
    Output: NONE
    END OF EXAMPLE
    
    EXAMPLE
    Conversation history:
    Mark: What do you know about Descartes?
    Sam: Descartes was a French philosopher, mathematician, and scientist who lived in the 17th century.
    Mark: The Descartes I'm referring to is a standup comedian and interior designer from Montreal.
    Sam: Oh yes, He is a comedian and an interior designer. He has been in the industry for 30 years. His favorite food is baked bean pie.
    Mark: Oh huh. I know Descartes likes to drive antique scooters and play the mandolin.    
    Output: (Descartes, likes to drive, antique scooters)<|>(Descartes, plays, mandolin)
    END OF EXAMPLE
    
    Conversation history:
    {history}
    Current Input:
    {input}
    Output: """
)

KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["history", "input"],
    template=KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE,
)

SENTIMENT_ANALYSIS_TEMPLATE = (
    """Your job is to analyze the current input in a given conversation and provide a simple sentiment analysis as output. The simple sentiment analysis is a description of the emotional tone of the message. A positive input will convey happiness, optimism, satisfaction, or excitement. A negative input will convey sadness, anger, disappointment, or fear. A neutral input will convey no emotion or a neutral emotion. The sentiment analysis should be based on the current input only, and not on the entire conversation history, which is only provided for context.
    
    EXAMPLE
    Conversation history:
    James: How are you things at work?
    Stewart: Super! I just finished a project I've been working on forever.
    James: Splendid! Congratulations!
    Current Input:
    Stewart: Thanks! I'm think I got a shot at that promotion.
    Output: Positive. Stewart is optimistic about his promotion.
    END OF EXAMPLE
    
    EXAMPLE
    Conversation history:
    Sally: Hey, how is school going?
    Beth: Fine, thanks. Just a bit busy with homework.
    Sally: I see. Well, do you need some help?
    Current Input:
    Beth: Eh, maybe later. I'm just going to get some rest.
    Output: Neutral. Beth is not expressing any emotion.
    END OF EXAMPLE
    
    EXAMPLE
    Conversation history:
    Amy: How did the presentation go today?
    Peter: Terrible! My car broke down, and I arrived late!
    Amy: Oh no! I'm so sorry to hear that! Can you reschedule?
    Current Input:
    Peter: Ugh, no! They already went with another firm, and I'm afraid I could lose my job.
    Output: Negative. Peter is feeling disappointed and is afraid he is losing his job.
    END OF EXAMPLE
    
    Conversation history (For reference only):
    {history}
    Current Input (For sentiment analysis):
    {input}
    Output: """
)

SENTIMENT_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["history", "input"],
    template=SENTIMENT_ANALYSIS_TEMPLATE,
)
