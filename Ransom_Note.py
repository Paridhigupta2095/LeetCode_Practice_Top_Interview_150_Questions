from collections import Counter
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # solution 2
        mag=Counter(magazine)
        ran= Counter(ransomNote)

        for char in ran.keys():
            mag[char]-=ran[char]
            if(mag[char]<0):
                return False
        return True

# ---------------- Driver Code ----------------
if __name__ == "__main__":
    sol = Solution()
    
    # List of test cases as tuples (ransomNote, magazine)
    test_cases = [
        ("a", "b"),           # False
        ("aa", "ab"),         # False
        ("aa", "aab"),        # True
        ("abc", "aabbcc"),    # True
        ("aab", "abbc"),      # False
    ]
    
    # Run each test case
    for i, (ransomNote, magazine) in enumerate(test_cases, 1):
        result = sol.canConstruct(ransomNote, magazine)
        print(f"Test case {i}: canConstruct('{ransomNote}', '{magazine}') → {result}")

            
            

        


        