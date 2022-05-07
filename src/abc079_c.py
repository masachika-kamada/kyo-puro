def main():
#     import io
#     import sys

#     _INPUT = """\
# 1222

#     """
#     sys.stdin = io.StringIO(_INPUT)

    s = input()
    n2 = 1 << 3  # 左シフト i.e. n2 = 2^n
    for t in range(n2):
        ops = ["-"] * 3
        for i in range(3):
            # <bit全探索>
            # t(カウント)を選ぶ・選ばないを判断したい桁数分右シフト
            # i.e. 末尾の桁を消す
            # カウントをi回右にシフトして1と論理積を取る
            # i.e. 最下位の桁が1かどうかチェックする
            if (t >> i) & 1:
                ops[i] = "+"  # データのi番目に対して処理を実行
        formula = s[0] + ops[0] + s[1] + ops[1] + s[2] + ops[2] + s[3]
        if eval(formula) == 7:
            print(f"{formula}=7")
            break


main()
