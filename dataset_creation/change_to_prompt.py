import json
from argparse import ArgumentParser

from generate_txt_dataset import DELIMITER_0, DELIMITER_1, STOP


def main(input_path: str, output_path: str):
    with open(input_path) as f:
        prompts = [json.loads(l) for l in f]

    with open(output_path, "w") as f:
        for prompt in prompts:
            url = "url"
            f.write(f"{json.dumps(dict(caption=prompt['input'], edit=prompt['edit'], output=prompt['output'], url=url))}\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input-path", required=True, type=str)
    parser.add_argument("--output-path", required=True, type=str)
    args = parser.parse_args()
    main(args.input_path, args.output_path)
