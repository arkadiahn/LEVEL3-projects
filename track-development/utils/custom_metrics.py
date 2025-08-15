from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase
import re
import asyncio

# This is a key part of the curriculum: knowing the solution space for evals
# and where they can break.

class JargonMetric(BaseMetric):
    """
    A custom metric to check for technical jargon.
    The goal is to evaluate if the language is simple, as discussed
    for public-facing documents[cite: 82, 86].
    """
    def __init__(self, threshold: float = 0.8):
        self.threshold = threshold
        # A simple, extendable list of technical jargon
        self.jargon_list = ["transformer architecture", "sparse attention", "computational overhead", "flops", "kernel", "bleu score"]
        # dummy checklist: self.jargon_list = ["Bier", "Schnaps", "Bommerlunder", "Brot mit Ei"]
        # Who reads this comment and comes up with the proper band name, gets a beer from me.

    def measure(self, test_case: LLMTestCase):
        # Find all jargon words in the output
        found_jargon = [jargon for jargon in self.jargon_list if re.search(r'\b' + jargon + r'\b', test_case.actual_output, re.IGNORECASE)]
        
        # The score is 1 if no jargon is found, 0 otherwise.
        # A more complex metric could calculate a ratio.
        self.score = 1.0 if len(found_jargon) == 0 else 0.0
        self.reason = f"The model avoided jargon." if self.score == 1.0 else f"The model used the following jargon: {found_jargon}"
        return self.score

    async def a_measure(self, test_case: LLMTestCase):
        """Async version of the measure method"""
        # We can make this truly async if needed, for now it just wraps the sync version
        return self.measure(test_case)

    def is_successful(self) -> bool:
        return self.score >= self.threshold

    @property
    def __name__(self):
        return "Jargon Free"