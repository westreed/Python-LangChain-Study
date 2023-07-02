import util
from pprint import pprint
from data_manager import DataManager, MemoryManager, KeyManager
from core.create_question import create_question


def input_process(manager: DataManager):
    input_data = util.input_user_info()
    if input_data is False:
        return False
    manager.set_data(input_data)


if __name__ == "__main__":
    key_manager = KeyManager()
    data_manager = DataManager()
    memory_manager = MemoryManager()
    input_process(data_manager)
    pprint(f"DataManager : {data_manager.get_data()}")

    create_question(data_manager, memory_manager, key_manager)