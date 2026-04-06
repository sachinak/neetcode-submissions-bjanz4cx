class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "[]"
        res = ".".join(strs)
        return res
    def decode(self, s: str) -> List[str]:
        if s=="[]":
            return []
        res = s.split(".")
        return res