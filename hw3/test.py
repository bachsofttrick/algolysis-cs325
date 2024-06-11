from DNAMatch import dna_match_topdown, dna_match_bottomup

def run_tests():
    test_string = ['ATAGTTCCGTCAAA','GTGTTCCCGTCAAA','GTGTTCCCGTCAAA','','GTCAATCCGTTCCCAA','GTCAATCCGTTCCCAA','AT','G']

    for i in range(0, len(test_string), 2):
        DNA1 = test_string[i]
        DNA2 = test_string[i + 1]
        print("DNA1:", DNA1)
        print("DNA2:", DNA2)
        topdown_result = dna_match_topdown(DNA1, DNA2)
        bottomup_result = dna_match_bottomup(DNA1, DNA2)
        print("Length of the best continuous length of the DNA string alignment (Top-down):", topdown_result)
        print("Length of the best continuous length of the DNA string alignment (Bottom-up):", bottomup_result)
        if topdown_result == bottomup_result:
            print("Success")
        else:
            print("Fail")
        print()

if __name__ == "__main__":
    run_tests()


