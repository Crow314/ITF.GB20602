import re


def main(string: str):
    substr = re.match(r'\A(.+?)\1*\Z', string).groups()[0]
    print(int(len(string) / len(substr)))


if __name__ == '__main__':
    while True:
        s = input()
        if '.' in s:
            break

        main(s)
