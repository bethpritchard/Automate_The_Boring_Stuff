
A = [1,2,3,4,5]
K = 3

#
def solution(A, K):
    count = 0
    while count < K:
        count += 1
        last = A[-1]
        for i in range(1,len(A)):
            A[len(A)-i] = A[len(A)-(i+1)]
        A[0] = last
        return A



print(solution(A,K))

