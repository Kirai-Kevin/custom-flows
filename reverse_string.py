# reverse_string.py

from pydantic import BaseModel
from asyncflows import Action

class Inputs(BaseModel):
    input_string: str
    word_index: int = 0

class Outputs(BaseModel):
    reversed_string: str

class MyReverseString(Action[Inputs, Outputs]):
    name = 'my_reverse_string'

    async def run(self, inputs: Inputs) -> Outputs:
        words = inputs.input_string.split()
        if 0 <= inputs.word_index < len(words):
            words[inputs.word_index] = words[inputs.word_index][::-1]
        
        reversed_string = ' '.join(words)
        
        return Outputs(
            reversed_string=reversed_string
        )
