class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in "[{(":
                st.append(char)
            elif len(st) != 0 and ((char == "]" and st[-1] == "[") or (char == "}" and st[-1] == "{") or (char == ")" and st[-1] == "(")):
                st.pop()
            else:
                return False
        if len(st) == 0:
            return True
        else:
            return False
