# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#marksheet = []
#for _ in range(0,int(input())):
#    marksheet.append([input(), float(input())])
#
#second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
#print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] 

        for a, c in sorted(marksheet):
             if c==b:
                print(a)