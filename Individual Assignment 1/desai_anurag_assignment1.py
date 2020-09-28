def student_score(student_id):
    """
    This function would create a score list for every student
    :param student_id: The identifier for the students
    :return: A list of all the scores of the student
    """
    more_student_scores = True
    score_list = []
    while more_student_scores:
        score = input("Please enter Student "+str(student_id)+"'s score (-1: Exit): ")
        if score.isdecimal():
            score_list.append(int(score))
        elif score == "-1":
            more_student_scores = False
        else:
            print("The score entered is not a number. Please enter it again")
    return score_list


def print_scores(score_list, student_id):
    """
    This function is a simple printing function for scores of all the students
    :param score_list: List of all the scores for particular student
    :param student_id: The id of student
    :return: None
    """
    print("Student " + str(student_id) + " took " + str(len(score_list)) + " exams")
    print("Average Score: " + str(int(sum(score_list)/len(score_list))))
    print("Highest Score: " + str(max(score_list)))
    print("Lowest Score: " + str(min(score_list)))


def main():
    more_students = True
    student_id = 1
    more_students_input = "yes"
    final_score_list = []
    while more_students:
        if more_students_input.lower() == "yes":
            final_score_list.insert(student_id, student_score(student_id))
            student_id += 1
            more_students_input = input("Any more student? (Yes or No): ")
        else:
            more_students = False
            [print_scores(final_score_list[i], i + 1) for i in range(len(final_score_list))]


if __name__ == "__main__":
    main()