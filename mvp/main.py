import util
from pprint import pprint
from data_manager import *
from core.init_question_generator import init_question_generator
from core.evaluate_input_info import evaluate_input_info
from core.question_and_answer import question_and_answer
from core.follow_up_question_generator import follow_up_question_generator


def input_process(manager: DataManager):
    # input.json에서 데이터를 가져옵니다.
    input_data = util.input_user_info()
    if input_data is False:
        return False
    manager.set_data(input_data)


if __name__ == "__main__":
    # 전역으로 관리하기 위해 생성된 Manager
    key_manager = KeyManager()
    data_manager = DataManager()
    evaluation_manager = EvaluationManager()

    # input_process에서 사용자의 데이터(input.json)를 읽어서, DataManager에 저장함.
    input_process(data_manager)
    pprint(f"DataManager : {data_manager.get_data()}")
    print("----------------------------------------")

    # Input으로 받은 회사모집공고와 자소서, 1분 자기소개를 바탕으로 평가를 생성합니다.
    evaluate_input_info(data_manager, evaluation_manager)

    print("----------------------------------------")

    # CreateQuestion 함수에서 초기질문을 생성합니다.
    question_list = init_question_generator(data_manager)
    # 생성된 질문리스트를 QuestionManager에 저장합니다.
    question_manager = QuestionManager(question_list)

    print("----------------------------------------")

    for _ in range(6):
        # 생성된 question_list에서 질문을 1개씩 가져와서, 질문을 던집니다.
        # question_and_answer 함수는 인자로 받은 질문을 던지고, 답변 내용을 평가합니다.
        question_and_answer(data_manager, QuestionEntity(question_manager.get_question()), evaluation_manager)

        print("----------------------------------------")

        for _ in range(3):
            # question_and_answer 함수의 결과가 나왔다면, 심화질문 생성함수를 실행합니다.
            # 생성결과 심화질문이 필요없다고 판단되면 "Very nice good!"을 return 합니다.
            followup = follow_up_question_generator(data_manager, evaluation_manager)
            if followup == "Very nice good!":
                break

            # 심화질문이 생성되었다면, 다시 question_and_answer 함수로 질문과 답변을 받고 평가합니다.
            # 심화질문에 대한 평가가 EvaluationManager에 저장되어서 다음 반복문에서 이 결과를
            # 이용해서 심화질문을 또 생성하게 됩니다. 일단, 최대 3회 반복합니다.
            question_and_answer(
                data_manager,
                QuestionEntity(followup),
                evaluation_manager
            )
