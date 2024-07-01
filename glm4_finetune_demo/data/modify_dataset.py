import json

def convert_dataset(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line)
            input_text = data.get("input", "")
            output_text = data.get("output", "")
            instruction = data.get("instruction", "")

            converted_entry = {
                "messages": [
                    {
                        "role": "system",
                        "content": instruction
                    },
                    {
                        "role": "user",
                        "content": input_text
                    },
                    {
                        "role": "assistant",
                        "content": output_text
                    }
                ]
            }

            json.dump(converted_entry, outfile, ensure_ascii=False)
            outfile.write('\n')

# 使用示例
input_file = 'dev.jsonl'
output_file = 'dev_.jsonl'
convert_dataset(input_file, output_file)
