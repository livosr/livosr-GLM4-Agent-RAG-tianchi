from pathlib import Path
from typing import Annotated, Union

import json

import typer
from peft import AutoPeftModelForCausalLM, PeftModelForCausalLM
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    PreTrainedTokenizerFast
)

ModelType = Union[PreTrainedModel, PeftModelForCausalLM]
TokenizerType = Union[PreTrainedTokenizer, PreTrainedTokenizerFast]

app = typer.Typer(pretty_exceptions_show_locals=False)


def load_model_and_tokenizer(
        model_dir: Union[str, Path], trust_remote_code: bool = True
) -> tuple[ModelType, TokenizerType]:
    model_dir = Path(model_dir).expanduser().resolve()
    if (model_dir / 'adapter_config.json').exists():
        model = AutoPeftModelForCausalLM.from_pretrained(
            model_dir, trust_remote_code=trust_remote_code, device_map='auto'
        )
        tokenizer_dir = model.peft_config['default'].base_model_name_or_path
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_dir, trust_remote_code=trust_remote_code, device_map='auto'
        )
        tokenizer_dir = model_dir
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_dir, trust_remote_code=trust_remote_code, encode_special_tokens=True, use_fast=False
    )
    return model, tokenizer


@app.command()
def main(
        model_dir: Annotated[str, typer.Argument(help='')],
):
    model, tokenizer = load_model_and_tokenizer(model_dir)
    with open("./data/dev_.jsonl", "r") as f:
        lines = f.readlines()

    for line in lines:
        print("=========")
        messages_dev = json.loads(line)['messages']
        messages = []
        for message in messages_dev:
            # print(message)
            if message["role"] != "assistant":
                messages.append(message)
            if message["role"] == "user":
                print("question: {}".format(message["content"]))


        # exit(0)
        
        inputs = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_tensors="pt"
        ).to(model.device)
        generate_kwargs = {
            "input_ids": inputs,
            "max_new_tokens": 1024,
            "do_sample": True,
            "top_p": 0.8,
            "temperature": 0.8,
            "repetition_penalty": 1.2,
            "eos_token_id": model.config.eos_token_id,
        }
        outputs = model.generate(**generate_kwargs)
        response = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True).strip()
        
        print("answer: {}".format(response))
        


if __name__ == '__main__':
    app()
