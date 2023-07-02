import json

INPUT_FILE_NAME = "input"


def input_user_info():
    try:
        with open(f"{INPUT_FILE_NAME}.json", "r", encoding="UTF-8") as f:
            input_data = json.load(f)

    except FileNotFoundError:
        # input.json 파일이 없음.
        with open(f"{INPUT_FILE_NAME}.json", "w", encoding="UTF-8") as f:
            f.write(
                """{
    "user_company" : "",
    "user_job" : "",
    "job_requirement" : "",
    "cover_letter" : ""
}"""
            )
        print("input.json을 열고, 정보를 작성하세요.")
        return False
    
    return input_data
