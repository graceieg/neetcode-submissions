class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}  # key: sorted word, value: list of words

        for word in strs:
            # Sort the word to create a key
            key = ''.join(sorted(word))
            
            # Add the word to the correct group
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]

        # Return all grouped anagrams as a list of lists
        return list(anagram_map.values())

       
