def input_students():   # 학생 정보를 입력하는 함수
    students = []
    for i in range(5): 
        student_id = input("학번: ")
        name = input("이름: ")
        scores = []
        for subject in ['영어', 'C-언어', '파이썬']: 
            score = float(input(f"{subject}: "))
            scores.append(score)
        students.append({'student_id': student_id, 'name': name, 'scores': scores})
        print()
    return students

def calculate_total(scores):  # 총점을 계산하는 함수
    return sum(scores)


def calculate_average(scores):  # 평균을 계산하는 함수
    return sum(scores) / len(scores)


def calculate_grade(scores):  # 학점을 계산하는 함수
    ave = sum(scores) / len(scores) 
    if ave >= 95:
        return "A+"
    elif ave >= 90:
        return "A"
    elif ave >= 85:
        return "B+"
    elif ave >= 80:
        return "B"
    elif ave >= 75:
        return "C+"
    elif ave >= 70:
        return "C"
    elif ave >= 65:
        return "D+"
    elif ave >= 60:
        return "D"
    else:
        return "F"


def calculate_rank(students): # 등수를 계산하여 학생에게 할당하는 함수
    students.sort(key=lambda x: calculate_average(x['scores']), reverse=True)
    for i, student in enumerate(students):
        student['average_rank'] = i + 1
    return students


def output_students(students): # 학생 정보 출력 함수
    print("\n\n")
    print("==============================================================================================")
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("==============================================================================================")

    for student in students:
        total_score = calculate_total(student['scores'])
        average_score = calculate_average(student['scores'])
        grade = calculate_grade(student['scores'])
        rank = student['average_rank'] 
        print(f"{student['student_id']}\t{student['name']}\t{student['scores'][0]}\t{student['scores'][1]}\t{student['scores'][2]}\t{total_score}\t{average_score:.2f}\t{grade}\t{rank}")
def add_student(students):
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    scores = []
    for subject in ['영어', 'C-언어', '파이썬']:
        score = float(input(f"{subject} 점수를 입력하세요: "))
        scores.append(score)
    students.append({'student_id': student_id, 'name': name, 'scores': scores})
    print("학생 정보가 추가되었습니다.\n")
    return students  # 수정된 students 리스트를 반환

def remove_student(students):
    identifier = input("삭제할 학생의 학번 또는 이름을 입력하세요: ")
    found = False
    for student in students:
        if student["student_id"] == identifier or student["name"] == identifier:
            students.remove(student)
            print("학생 정보가 삭제되었습니다.\n")
            found = True
            break  # 삭제 후 반복문 종료
    if not found:
        print("해당하는 학생이 없습니다.\n")
    return students  # 수정된 students 리스트를 반환

def find_student(students):
    identifier = input("탐색할 학생의 학번 또는 이름을 입력하세요: ")
    found_students = [student for student in students if student["student_id"] == identifier or student["name"] == identifier]
    if found_students:
        for student in found_students:
            print(f"학번: {student['student_id']}, 이름: {student['name']}, 점수: {student['scores']}")
    else:
        print("해당하는 학생이 없습니다.\n")
        if input("새로운 학생을 추가하시겠습니까? (yes/no): ").lower() == "yes":
            students = add_student(students)  # 새로운 학생 추가
    return students  # 수정된 students 리스트를 반환

def count_students_above_80(students):
    count = sum(1 for student in students if sum(student["scores"]) / len(student["scores"]) >= 80)
    print(f"평균 점수가 80점 이상인 학생의 수: {count}\n")


# 전역 변수로 students 리스트 선언
students = []
students_with_rank = []

students = input_students()  # 학생 정보 입력하기
students_with_rank = calculate_rank(students)  # 등수 계산하기
output_students(students_with_rank)  # 학생 정보 출력하기

def main_menu():
    global students, students_with_rank
    while True:
        print("\n[학생 정보 관리 시스템]")
        print("1: 학생 정보 입력")
        print("2: 학생 정보 삭제")
        print("3: 학생 정보 탐색")
        print("4: 평균 80점 이상 학생 수 카운트")
        print("5: 학생 정보 출력")
        print("6: 종료")
        choice = input("선택: ")

        if choice == "1":
            students = input_students()
            students_with_rank = calculate_rank(students)
        elif choice == "2":
            students = remove_student(students)
        elif choice == "3":
            students = find_student(students)
        elif choice == "4":
            count_students_above_80(students)
        elif choice == "5":
            if students_with_rank:  # students_with_rank가 초기화되었는지 확인
                output_students(students_with_rank)
            else:
                print("학생 정보가 없습니다.\n")
        elif choice == "6":
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.\n")

# 프로그램 시작 시 main_menu 함수 호출
if __name__ == "__main__":
    main_menu()