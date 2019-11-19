# -*- encoding: utf-8 -*-
import my_function

def test_primes_list_bw():
    assert my_function.primes_list_bw(18) == [2, 3, 5, 7, 11, 13, 17]
    assert my_function.primes_list_bw(100) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 
        71, 73, 79, 83, 89, 97]
    assert my_function.primes_list_bw(1000) == [2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 
        103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
        179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
        257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 
        347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 
        431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 
        509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 
        607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 
        691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
        797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 
        883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 
        991, 997]

def test_sum_divis():
    assert my_function.sum_divis(18) == [1, 2, 9, 3, 6]
    assert my_function.sum_divis(40) == [1, 2, 20, 4, 10, 5, 8]
    assert my_function.sum_divis(1000) == [1, 2, 500, 4, 250, 5, 200, 8, 125, 
        10, 100, 20, 50, 25, 40]

def test_divisibility_num_by_all_in_tuple():
    assert my_function.divisibility_num_by_all_in_tuple(1000, 
        [1, 2, 500, 4, 250, 5, 200, 8, 125, 10, 100, 20, 50, 25, 40]) == True
    assert my_function.divisibility_num_by_all_in_tuple(500,
        [1, 2, 500, 4, 250, 5, 125, 10, 100, 20, 50, 25, 200]) == False
    assert my_function.divisibility_num_by_all_in_tuple(250, 
        [1, 2, 500, 4, 250, 5, 200, 8, 125, 10, 100, 20, 50, 25, 40]) == False
    assert my_function.divisibility_num_by_all_in_tuple(-1000, 
        [1, 2, 500, 4, 250, 5, 200, 8, 125, 10, 100, 20, 50, 25, 40]) == True
    assert my_function.divisibility_num_by_all_in_tuple(1000.00, 
        [1, 2, 500, 4, 250, 5, 200, 8, 125, 10, 100, 20, 50, 25, 40]) == True
    assert my_function.divisibility_num_by_all_in_tuple(1000.00, 
        [1, 2, 500, 4, 250, 5.00, 200, 8, 125, 10, 100, 20.00, 50, 25, 40]
        ) == True
    assert my_function.divisibility_num_by_all_in_tuple(1000.00,
        [1, 2, 500, 4, 250, 5, 200, 8, 125, 10, 100, 20, 50.05, 25, 40]
        ) == False

def test_eng_letter_to_num():
    assert my_function.eng_letter_to_num('a') == 1
    assert my_function.eng_letter_to_num('A') == 1
    assert my_function.eng_letter_to_num('b') == 2
    assert my_function.eng_letter_to_num('B') == 2
    assert my_function.eng_letter_to_num('c') == 3
    assert my_function.eng_letter_to_num('C') == 3
    assert my_function.eng_letter_to_num('d') == 4
    assert my_function.eng_letter_to_num('D') == 4
    assert my_function.eng_letter_to_num('e') == 5
    assert my_function.eng_letter_to_num('E') == 5
    assert my_function.eng_letter_to_num('f') == 6
    assert my_function.eng_letter_to_num('F') == 6
    assert my_function.eng_letter_to_num('g') == 7
    assert my_function.eng_letter_to_num('G') == 7
    assert my_function.eng_letter_to_num('h') == 8
    assert my_function.eng_letter_to_num('H') == 8
    assert my_function.eng_letter_to_num('i') == 9
    assert my_function.eng_letter_to_num('I') == 9
    assert my_function.eng_letter_to_num('j') == 10
    assert my_function.eng_letter_to_num('J') == 10
    assert my_function.eng_letter_to_num('k') == 11
    assert my_function.eng_letter_to_num('K') == 11
    assert my_function.eng_letter_to_num('l') == 12
    assert my_function.eng_letter_to_num('L') == 12
    assert my_function.eng_letter_to_num('m') == 13
    assert my_function.eng_letter_to_num('M') == 13
    assert my_function.eng_letter_to_num('n') == 14
    assert my_function.eng_letter_to_num('N') == 14
    assert my_function.eng_letter_to_num('o') == 15
    assert my_function.eng_letter_to_num('O') == 15
    assert my_function.eng_letter_to_num('p') == 16
    assert my_function.eng_letter_to_num('P') == 16
    assert my_function.eng_letter_to_num('q') == 17
    assert my_function.eng_letter_to_num('Q') == 17
    assert my_function.eng_letter_to_num('r') == 18
    assert my_function.eng_letter_to_num('R') == 18
    assert my_function.eng_letter_to_num('s') == 19
    assert my_function.eng_letter_to_num('S') == 19
    assert my_function.eng_letter_to_num('t') == 20
    assert my_function.eng_letter_to_num('T') == 20
    assert my_function.eng_letter_to_num('u') == 21
    assert my_function.eng_letter_to_num('U') == 21
    assert my_function.eng_letter_to_num('v') == 22
    assert my_function.eng_letter_to_num('V') == 22
    assert my_function.eng_letter_to_num('w') == 23
    assert my_function.eng_letter_to_num('W') == 23
    assert my_function.eng_letter_to_num('x') == 24
    assert my_function.eng_letter_to_num('X') == 24
    assert my_function.eng_letter_to_num('y') == 25
    assert my_function.eng_letter_to_num('Y') == 25
    assert my_function.eng_letter_to_num('z') == 26
    assert my_function.eng_letter_to_num('Z') == 26

def test_route_table():
    assert my_function.route_table(30) == 118264581564861424
    assert my_function.route_table(2) == 6
    assert my_function.route_table(9) == 48620
    assert my_function.route_table(17) == 2333606220
    assert my_function.route_table(20) == 137846528820
    assert my_function.route_table(25) == 126410606437752

def test_factorization():
    assert my_function.factorization(30) == [2, 3, 5]
    assert my_function.factorization(4) == [2, 2]
    assert my_function.factorization(10) == [2, 5]
    assert my_function.factorization(100) == [2, 2, 5, 5]
    assert my_function.factorization(1020) == [2, 2, 3, 5, 17]
    assert my_function.factorization(888) == [2, 2, 2, 3, 37]
    assert my_function.factorization(578) == [2, 17, 17]
    assert my_function.factorization(3578) == [2, 1789]
    assert my_function.factorization(422222) == [2, 107, 1973]
    assert my_function.factorization(90) == [2, 3, 3, 5]
    assert my_function.factorization(64) == [2, 2, 2, 2, 2, 2]
    assert my_function.factorization(225) == [3, 3, 5, 5]

def test_sumdivis():
    assert my_function.sumdivis(1) == 1
    assert my_function.sumdivis(4) == 3
    assert my_function.sumdivis(14) == 10
    assert my_function.sumdivis(16) == 15
    assert my_function.sumdivis(160) == 218
    assert my_function.sumdivis(562) == 284
    assert my_function.sumdivis(1024) == 1023
    assert my_function.sumdivis(361024) == 355510
    assert my_function.sumdivis(79068) == 122532
    assert my_function.sumdivis(1010107) == 155429

def test_summ_factorial_num():
    assert my_function.summ_factorial_num(10) == 2
    assert my_function.summ_factorial_num(15) == 121
    assert my_function.summ_factorial_num(109732) == 367930
    assert my_function.summ_factorial_num(54) == 144
    assert my_function.summ_factorial_num(15408) == 40466
    assert my_function.summ_factorial_num(894345738742) == 453806
    assert my_function.summ_factorial_num(10203040) == 37
    assert my_function.summ_factorial_num(120140160) == 752
    assert my_function.summ_factorial_num(5999999998) == 2943480
    assert my_function.summ_factorial_num(546030000000) == 878

def test_isPrime():
    assert my_function.isPrime(2) == True
    assert my_function.isPrime(12) == False
    assert my_function.isPrime(17) == True
    assert my_function.isPrime(15) == False
    assert my_function.isPrime(201) == False
    assert my_function.isPrime(7097) == False
    assert my_function.isPrime(120002) == False
    assert my_function.isPrime(7193) == True
    assert my_function.isPrime(9067) == True
    assert my_function.isPrime(20100000) == False
    assert my_function.isPrime(997) == True
    assert my_function.isPrime(84587539377) == False
    assert my_function.isPrime(84587539373) == True
    assert my_function.isPrime(7734273) == False
    assert my_function.isPrime(7734317) == True

def test_isnotPrime():
    assert my_function.isnotPrime(2) == False
    assert my_function.isnotPrime(12) == True
    assert my_function.isnotPrime(17) == False
    assert my_function.isnotPrime(15) == True
    assert my_function.isnotPrime(201) == True
    assert my_function.isnotPrime(7097) == True
    assert my_function.isnotPrime(120002) == True
    assert my_function.isnotPrime(7193) == False
    assert my_function.isnotPrime(9067) == False
    assert my_function.isnotPrime(20100000) == True
    assert my_function.isnotPrime(997) == False
    assert my_function.isnotPrime(84587539377) == True
    assert my_function.isnotPrime(84587539373) == False
    assert my_function.isnotPrime(7734273) == True
    assert my_function.isnotPrime(7734317) == False
