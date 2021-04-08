import subprocess as sbp
from settings import get_path


def main(path):
    with open("lecture_name_in.txt", mode="r", encoding="UTF-8") as file:
        input_string = file.read()
        input_list = list(input_string.split("\n"))
        for name in input_list:
            if name == "":
                continue
            sbp.run(["mkdir", name], cwd=path, shell=True)
            lec_path = path + "\\" + f"{name}"
            for i in range(1, 15):
                tmp = name + f"_{i}"
                sbp.run(["mkdir", tmp], cwd=lec_path, shell=True)


if __name__ == '__main__':
    main(get_path())
