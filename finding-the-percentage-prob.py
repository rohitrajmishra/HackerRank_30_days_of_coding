if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks_list = student_marks[query_name]
    sum = 0
    for i in marks_list:
        sum += i

    average_marks = sum / len(marks_list)
    print("%.2f" % (average_marks))

