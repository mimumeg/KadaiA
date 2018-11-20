# A-1: 文字列のリスト
# "Bob", "Tom", "Ken" という3つの文字列要素を持つusersというリストを定義してください
from typing import List

users = ["Bob", "Tom", "Ken"]

# A-2: 整数のリスト
# 1から5までの整数を要素として持つint_numbersリストを定義してください
# int_numbers = [1, 2, 3, 4, 5]
int_number = list(range(1, 6))
print(int_number)

# A-3: 要素のデータ型が異なるリスト
# "Kazuma", "Takahashi", 35 という 3つの要素をもつkazuma_infoというリストを定義してください
kazuma_info = ["Kazuma", "Takahashi", 35]

# A-4: 要素へのアクセス
# 次のmembersというリストから "Makoto" と "Kazuma" を取得して出力してください
members = ["Kazuma", "Makoto", "Ohira"]

print(members[1])
print(members[2])

# A-5:  要素へのアクセスとフォーマット
# 次のリストを利用して、"Name: Takahashi Kazuma, Age: 35"と出力してください
print(f'Name: {kazuma_info[1]} {kazuma_info[0]}, Age: {kazuma_info[2]}')

# A-6: forによるループその1
# for を使って odd_numbers の各要素を出力してください

odd_numbers = [1, 3, 5, 7, 9]
for odd_number in odd_numbers:
    print(odd_number)

print()

# A-7: forによるループその2
# for を使って even_numbers のそれぞれの値を2倍した値を出力してください

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

def info_print(name, age):
    print(f"Name: {name}, Age: {age}")


users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]


# A-9: 辞書
# 下記のコードが期待通り動作するような辞書を定義してください

# def kazuma_info(fist_name, family_name, age):
#     kazuma_info = ["Kazuma", "Takahashi", 35]
#
#
# print(kazuma_info["first_name"])  # "Kazuma"
# print(kazuma_info["family_name""]) # "
# Takahashi
# "
# print(kazuma_info["age"])  # 35
