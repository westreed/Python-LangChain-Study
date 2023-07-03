import util
from pprint import pprint
from data_manager import *
from core.create_question import create_question
from core.evaluate_input_info import evaluate_input_info
from core.question_and_answer import question_and_answer
from core.follow_up_question import follow_up_question


def input_process(manager: DataManager):
    input_data = util.input_user_info()
    if input_data is False:
        return False
    manager.set_data(input_data)


if __name__ == "__main__":
    key_manager = KeyManager()
    data_manager = DataManager()
    evaluation_manager = EvaluationManager()
    input_process(data_manager)
    pprint(f"DataManager : {data_manager.get_data()}")
    print("----------------------------------------")

    evaluate_input_info(data_manager, evaluation_manager)

    print("----------------------------------------")

    question_list = create_question(data_manager)
    question_manager = QuestionManager(question_list)

    print(question_list)
    print("----------------------------------------")

    for i in range(3):

        question_and_answer(data_manager, question_manager, evaluation_manager)

        print("----------------------------------------")

        follow_up_question(data_manager, evaluation_manager)