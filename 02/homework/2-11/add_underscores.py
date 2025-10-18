#!/usr/bin/env python3
# coding=utf-8

# Podać sposób wyświetlania stringu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

word = "Python"
result = "_".join(word)

print(result)
assert result == "P_y_t_h_o_n"