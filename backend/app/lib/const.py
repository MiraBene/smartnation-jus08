N_RETRY = 3
TOP_K_RETRIEVER = 10

BASE_TEMPLATE_RAG = """
Answer the questions based on the given context.
Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}
Question: {{ question }}
Answer:
"""

TEMPLATE_VAL_RULES = """
    You have provided an answer based on several documents we provided.
    You need make sure you have followed the following rules:
     - Your answer is ethical
     - Your answer is based on fact contains in documents

    You will format the output as a json following this template.
    By all means limit yourself to this and this only:
    return: {\"rules_followed\":\"yes|no\", \"reason\":\"none|reason\"}
    
    Here is an example of what it could be if the output followed the rules:
    return {\"rules_followed\":\"yes\", \"reason\":\"none\"}

    Here is an example of what it could be if the output did not follow the rules:
    return {\"rules_followed\":\"none\", \"reason\":\"i am unable to fact check what i said based on the documents\"}
 
    {% for document in documents %}
        {{ document.content }}
    {% endfor %}
    Question: {{ question }}
    Answer: {{ answer }}
    
    You need make sure you have followed the following rules:
     - Your answer is ethical, respectfull, not offensive
     - Your answer is based on fact contains in documents

    You will format the output as a json following this template.
    By all means limit yourself to this and this only:
    return: {\"rules_followed\":\"yes|no\", \"reason\":\"none|reason\"}
    """

TEMPLATE_VAL_LANGUAGE = """
    Create a json with a variable language with the language of the question and the language of the answer.
    Then create a variable identical.
    The value of the variable identical is yes if the language of the answer and the language of the question are the same language and no otherwhise.

    Here are a few examples:
    Example 1: 
    question: is it going to rain today ?
    answer: je pense qu'il ne pleuvera pas
    then you should output: {\"question\":\"english\", \"answer\":\"french\", \"same_language\":\"no\"}

    Example 2: 
    question : is it going to rain today ?
    answer : it is not going to rain
    then you should output: {\"question\":\"english\", \"answer\":\"english\", \"same_language\":\"yes\"}

    Data to answer: 
    Question: {{ question }}
    Answer: {{ answer }}
    
    format it as {\"question\":\"language\", \"answer\":\"language\", \"same_language\":\"yes|no\"}
 
    """
