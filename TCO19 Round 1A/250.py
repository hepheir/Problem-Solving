def toBitArr(a):
    retval = []
    while a > 0:
        retval.append(a % 2)
        a = a >> 1
    return retval

def bitToDec(bit):
    retval = 0
    for i in range(len(bit)):
        retval += bit[i] * (2**i)
    return retval

def bitExtend(bit, length):
    return bit + [0]*(length-len(bit))

class EllysAndXor:
    def getMax(numbers):
        bins = []
        maxpos = 0
        nums = len(numbers)
        for dec in numbers:
            bit = toBitArr(dec)
            if len(bit) > maxpos:
                maxpos = len(bit)
            bins.append(bit)

        for i in range(nums):
            bins[i] = bitExtend(bins[i], maxpos)
        
        oplist = [0]*(maxpos-1) # mem what operation in order : and:0, xor:1
        isOplistDone = False
        posbits = []
        for pos in range(maxpos-1, -1, -1):
            posbit = [i[pos] for i in bins]
            posbits.append(posbit)
            if isOplistDone or not (1 in posbit):
                continue
            for i in range(nums-1, 0, -1):
                thisbit = posbit[i]
                nextbit = posbit[i-1]
                if thisbit != nextbit:
                    oplist[i] = 1
            isOplistDone = True

        print(oplist)
        print(posbits)
        finbit = [0]*maxpos
        for i in range(maxpos):
            posbit = posbits[i]
            for j in range(nums-1, 0, -1):
                if oplist[j] is 0:
                    posbit[j-1] = posbit[j] * posbit[j-1]
                else:
                    posbit[j-1] = (posbit[j] + posbit[j-1]) % 2
            finbit[i] = posbit[0]
        print(finbit)

        return bitToDec(finbit)


            

print(EllysAndXor.getMax((123,456,789,987,654,321)))