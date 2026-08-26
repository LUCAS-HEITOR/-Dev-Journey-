import random
from datasets import load_dataset

dataset = load_dataset("Hemg/AI-Generated-vs-Real-Images-Datasets", split="train")

Values = {0: "Real", 1: "AI"}

Correct= 0

def PrintarLogs(x: int):
    return f"has {x} correct answers" and x + 1


def main():
    while True:
        i = random.randint(0, len(dataset) - 1)
        example = dataset[i]

        image = example["image"]
        response_num = example["label"]
        response_text = Values[response_num]

        image.show()

        answer = int(input("This image (1) Real or (2) AI: "))



        if answer == response_text:
            PrintarLogs()
        else:
            print("Wrong")

main()
