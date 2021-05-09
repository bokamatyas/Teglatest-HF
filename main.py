from typing import List


def tégla_kalkulál(a: float, b: float, c: float) -> List:
    felszín = 2 * (a * b + a * c + b * c)
    térfogat = a * b * c
    if a <= 0 or b <= 0 or c <= 0:
        print('============================================')
        print('Egyik oldal sem lehet 0 vagy negatív érték!')
        exit()
    return [round(felszín, 3), round(térfogat, 3)]


print('Téglatést felszín-térfogat számoló program')
print('============================================')


def main() -> None:
    a = float(input('Kérem az a oldalt cm-ben: '))
    b = float(input('Kérem az b oldalt cm-ben: '))
    c = float(input('Kérem az c oldalt cm-ben: '))
    eredmény = tégla_kalkulál(a, b, c)
    print('============================================')
    print(f'A téglatest felszíne/térfogata: {eredmény}')


if __name__ == '__main__':
    main()
