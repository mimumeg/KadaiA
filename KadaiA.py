# A-1: 文字列のリスト
# "Bob", "Tom", "Ken" という3つの文字列要素を持つusersというリストを定義してください
from typing import List
import random

users = ["Bob", "Tom", "Ken"]

# A-2: 整数のリスト
# 1から5までの整数を要素として持つint_numbersリストを定義してください
# int_numbers = [1, 2, 3, 4, 5]
int_number = list(range(1, 6))
# print(int_number)

# A-3: 要素のデータ型が異なるリスト
# "Kazuma", "Takahashi", 35 という 3つの要素をもつkazuma_infoというリストを定義してください
kazuma_info = ["Kazuma", "Takahashi", 35]

# A-4: 要素へのアクセス
# 次のmembersというリストから "Makoto" と "Kazuma" を取得して出力してください
members = ["Kazuma", "Makoto", "Ohira"]

print(f"-----A-4:-----")
print(members[1])
print(members[2])
print()

# A-5:  要素へのアクセスとフォーマット
# 次のリストを利用して、"Name: Takahashi Kazuma, Age: 35"と出力してください
print(f"-----A-5:-----")
print(f'Name: {kazuma_info[1]} {kazuma_info[0]}, Age: {kazuma_info[2]}')
print()

# A-6: forによるループその1
# for を使って odd_numbers の各要素を出力してください
print(f"-----A-6:-----")
odd_numbers = [1, 3, 5, 7, 9]
for odd_number in odd_numbers:
    print(odd_number)

print()

# A-7: forによるループその2
# for を使って even_numbers のそれぞれの値を2倍した値を出力してください
print(f"-----A-7:-----")
even_numbers = [2, 4, 6, 8]
for even_number in even_numbers:
    result = even_number * 2
    print(result)
print()

# A-8: リストを要素に持つリスト
# users_info を使って次のような出力をしてください

# "Name: Kazuma, Age: 35"
# "Name: Tom, Age: 57"
# "Name: Bob, Age: 77"

print(f"-----A-8:-----")
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

users_element = 0

for users_name in users_info:
    print(f"Name: {users_info[users_element][0]}, Age: {users_info[users_element][1]}")
    users_element += 1

print()

# A-9: 辞書
# 下記のコードが期待通り動作するような辞書を定義してください
print(f"-----A-9:-----")
kazuma_info = {"first_name": "Kazuma", "family_name": "Takahashi", "age": 35}

print(kazuma_info["first_name"])  # "Kazuma"
print(kazuma_info["family_name"])  # "Takahashi"
print(kazuma_info["age"])  # 35

print()

# A-10: サイコロ
# 1から6の整数をランダムに出力する dice() 関数を実装してください
print(f"-----A-10:-----")


def dice():
    print(random.randint(1, 6))


dice()

# A-11: BMIアプリ
# 身長(m)と体重(kg)を入力として受け取りBMIを計算するアプリを実装してください
# 参考となるWebアプリ https://keisan.casio.jp/exec/system/1161228732​
# 小数点第2位まで表示すること
print(f"-----A-11:-----")


def bmi_calculator():
    height = float(input("身長を入力して下さい。(cm): "))  # 小数点に対応するfloat
    weight = float(input("体重を入力して下さい。(Kg): "))  # 小数点に対応するfloat

    # 身長・体重は小数点第2位表示なので再定義
    height = round(height, 2)
    weight = round(weight, 2)

    print(f'あなたの身長は{height}cm, 体重は{weight}Kgです')

    height = height * 0.01  # センチメートルからメートル変換

    bmi = weight / (height * height)

    # BMIは小数点第2位表示なので再定義
    bmi = round(bmi, 2)
    print(f"BMIは{bmi}です")


bmi_calculator()
