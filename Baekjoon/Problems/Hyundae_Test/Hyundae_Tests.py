# 현대 소프티어 모의
import sys
sys.stdin = open('input.txt')

def min_changes_to_consecutive_string(n, k, s):
    min_changes = float('inf')
    modified_string = ""

    for char in set(s):
        changes_required = 0
        current_modified = ""
        consecutive_count = 0

        for i in range(n):
            if s[i] == char:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count > k:
                changes_required += 1
                current_modified += char
            else:
                current_modified += s[i]

        if changes_required < min_changes:
            min_changes = changes_required
            modified_string = current_modified

    if min_changes == float('inf'):
        min_changes = 0

    print(min_changes)
    print(modified_string)

# 입력 받기
n, k = map(int, input().split())
s = input()

min_changes_to_consecutive_string(n, k, s)


