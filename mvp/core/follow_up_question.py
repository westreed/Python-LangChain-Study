from langchain import LLMChain
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.prompts import PromptTemplate

from mvp.data_manager import *
from mvp.util import remove_indent
from typing import *


def follow_up_question(
    data_manager: DataManager,
    evaluation_manager: EvaluationManager
):
    chat_manager = ChatManager()

    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                remove_indent(
                    f"""You are an interviewer at {data_manager.company}.

                    {data_manager.get_userdata()}
                    """)),

            HumanMessagePromptTemplate.from_template(
                remove_indent(
                    """You are an interviewer. Please read the interview question and response. If you determine that a `Follow up Question` is necessary, write the additional question you would like to ask in the areas for improvement. If you determine that it is not necessary, write `Very nice good!`. Also, please follow the format below when creating the questions:
                
                    ```
                    "심화질문":
                    - Content of follow up question
                    ```
                    And below is the interviewee's response to the interviewer's question, including the interviewer's evaluation:
                    {evaluation}
                    
                    Please write in Korean.
                    """))
        ],
        input_variables=["evaluation"],
    )

    followup_chain = LLMChain(llm=chat_manager.get_chat_model(),
                              prompt=prompt)
    output = followup_chain(evaluation_manager.get_answer_evaluation())
    from pprint import pprint
    pprint(output)
    
    # TODO: 심화질문 생성까지만 되어있고, 심화질문에 대한 답변과 평가를 해주는 시스템까지 완성하기
    # question and answer 파일을 심화질문에서도 쓸 수 있게 리팩토링하기
