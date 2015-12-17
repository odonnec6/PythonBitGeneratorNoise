
import PolyList

def generateBitSequence(numBits, polyNum):
    poly = PolyList.maximumLengthPolys[polyNum]
    # unsure about start state-- all ones for the time being
    startState = [1 for i in range(len(poly) - 1)]

    result = lfsr(poly, startState, numBits)
    asChars = list(map(str, result))

    return asChars

def lfsr(poly, startState, numBits):
    """
        Outputs a sequence with N elements. Each element is
        derived from successive values of the LFSR sequence
        generated by polynomial P and initial state S. Polynomial
        P is represented by a list of coefficients in decreasing
        power order.
        :param numBits: number of bits to generate
        :param startState: the starting state of the lfsr (array of ints)
        :param poly: the polynomial to be used (Poly class or array of ints)
    """
    def lfsr_internal():
        """
            Generates linear sequence according to polynomial
            P and initial state S.
        """
        seq, state = [startState[-1]], startState
        for j in range(2 ** len(startState) - 2):
            st0 = sum([i * j for i, j in zip(state, poly[1:])]) % 2
            state = [st0] + state[:-1]
            seq += [state[-1]]
        return seq

    assert len(poly) > 1 and len(poly) - 1 == len(startState)

    s = lfsr_internal()
    L = len(s)

    return [s[i % L] for i in range(numBits)]


print(generateBitSequence(10, 1))