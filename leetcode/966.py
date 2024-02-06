"""
https://leetcode.com/problems/vowel-spellchecker/
"""
from typing import List, Dict, Set, Optional


class Solution:
    def get_vowel_error_candidates(
        self, word: str, word_lower_dict: Dict[str, str]
    ) -> Set[str]:
        candidates: Set[str] = set()
        word_l = list(word.lower())

        for i, c in enumerate(word_l):
            if c in "aeiou":
                for alt in "aeiou":
                    cand = word_l[:i] + [alt] + word_l[i + 1 :]
                    candidates.add("".join(cand))
        return candidates

    def spellchecker(
        self, wordlist: List[str], queries: List[str]
    ) -> List[str]:
        answer: List[str] = []
        word_dict: Dict[str, str] = {word: word for word in wordlist}
        word_lower_dict: Dict[str, str] = {}
        for word in wordlist:
            if word.lower() not in word_lower_dict:
                word_lower_dict[word.lower()] = word
        for query in queries:
            if query in word_dict:
                answer.append(word_dict.get(query, ""))
                continue
            elif query.lower() in word_lower_dict:
                answer.append(word_lower_dict.get(query.lower(), ""))
                continue
            else:
                cands = self.get_vowel_error_candidates(query, word_lower_dict)
                print(f"{query} {cands}")
                match = cands.intersection(word_lower_dict.keys())
                print(match)
                if match:
                    answer.append(word_lower_dict.get(match.pop(), ""))
                else:
                    answer.append("")
        return answer


def main() -> None:
    sol = Solution()

    # Example Input
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = [
        "kite",
        "Kite",
        "KiTe",
        "Hare",
        "HARE",
        "Hear",
        "hear",
        "keti",
        "keet",
        "keto",
    ]

    result: List[str] = sol.spellchecker(wordlist, queries)

    # Example Output
    print(f"{result}")


main()
