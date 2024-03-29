# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result=sum(student_marks[query_name])/len(student_marks[query_name])
    # print(f"{result}")
    # print("{:.2f}".format(result)) # older syntax
    print("%.2f" % result)
