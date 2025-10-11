# Exercise: Matrix Script
# URL: https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
# Description: Turning a matrix into a string and decoding it without regex

n_row, n_col = map(int, input().split())
script_parts = []
script = ""

for _ in range(n_row):
    script_parts.append(input())

for i in range(n_col):
    for j in range(n_row):
        script += script_parts[j][i]

final_script_parts = []
final_script = ""
new_word = ""
for char in script:
    if char.isalpha():
        new_word += char
    elif new_word != "":
        final_script_parts.append(new_word)
        new_word = ""

for word in final_script_parts:
    final_script += word + " "

final_script = final_script.strip()
    
if final_script_parts != [] and not script[-1].isalpha():
    last_word = final_script_parts[-1]
    last_chars = script.split(last_word)[-1]
    final_script += last_chars

print(final_script)
