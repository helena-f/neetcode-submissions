class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groups = []
        anagram_indices = {}
        for string in strs:
            sorted_string = str(sorted(string))
            index_to_insert = anagram_indices.get(sorted_string, len(anagram_indices))
            anagram_indices[sorted_string] = index_to_insert
            print(index_to_insert)
            if len(anagram_indices) > len(anagram_groups):
                anagram_groups.append([string])
            else:
                anagram_groups[index_to_insert].append(string)
        
        print(anagram_groups)
        return anagram_groups

