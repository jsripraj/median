def medianMaintenance(filename):
    with open(filename, 'r') as file:
        # initialize A (max heap) and B (min heap)
        v = int(file.readline().strip())
        w = int(file.readline().strip())
        if v < w:
            A, B, medians = [v], [w], [v, v]
        else:
            A, B, medians = [w], [v], [v, w]
        sizeA, sizeB = 1, 1 
        for line in file:
            x = int(line.strip())
            # insert x into A or B
            if x < A[0] or (x > A[0] and x < B[0] and sizeA < sizeB):
                insertMaxHeap(A, x)
                sizeA += 1
            else:
                insertMinHeap(B, x)
                sizeB += 1
            # rebalance if necessary
            if sizeA-sizeB > 1:
                insertMinHeap(B, extractMax(A))
                sizeB += 1
                sizeA -= 1
            elif sizeB-sizeA > 1:
                insertMaxHeap(A, extractMin(B))
                sizeA += 1
                sizeB -= 1
            # compute median
            if (sizeA + sizeB)%2 == 0 or sizeA > sizeB:
                medians.append(A[0])
            else:
                medians.append(B[0])
    return medians
           
def swap(heap, i, j):
    temp = heap[i]
    heap[i] = heap[j]
    heap[j] = temp
    return

def insertMinHeap(heap, x):
    insert(heap, x, (lambda i,j: i<j))
    return

def insertMaxHeap(heap,x):
    insert(heap, x, (lambda i,j: i>j))
    return

def insert(heap, x, f):
    c = len(heap)
    heap.append(x)
    p = max((c-1)//2, 0)
    while f(heap[c], heap[p]):
        swap(heap, c, p)
        c = p
        p = max((c-1)//2, 0)
    return

def extractMin(heap):
    return extract(heap, (lambda i,j: i<j))

def extractMax(heap):
    return extract(heap, (lambda i,j: i>j))

def extract(heap, f):
    swap(heap, 0, len(heap)-1)
    answer = heap.pop()
    p, c1, c2 = 0, 1, 2
    while True:
        if c1 >= len(heap): # both c1 and c2 out of bounds
            break
        elif c2 >= len(heap): # only c2 is out of bounds
            if f(heap[c1], heap[p]):
                swap(heap, c1, p)
                p = c1
            else:
                break
        else: # both c1 and c2 are in bounds
            if f(heap[c1], heap[p]) and f(heap[c1], heap[c2]): 
                swap(heap, c1, p)
                p = c1
            elif f(heap[c2], heap[p]) and f(heap[c2], heap[c1]): 
                swap(heap, c2, p)
                p = c2
            else:
                break
        c1 = 2*p + 1
        c2 = c1+1
    return answer

filename = 'median.txt'
medians = medianMaintenance(filename)
answer = sum(medians) % len(medians)
# print('medians:', medians)
print('answer:', answer)