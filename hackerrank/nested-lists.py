# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students=[]
        students.append([name, score])
        lowest=min(score)
        for items in students:
            if lowest==min(score):
                students.remove(item)
        print(name, min(score))