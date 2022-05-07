def main():
#     import io
#     import sys

#     _INPUT = """\
# 4 2
# abi
# aef
# bc
# acg

#     """
#     sys.stdin = io.StringIO(_INPUT)

    # nが小さいので全探索可能（bit全探索）
    # itertools.combinations(s, i)でiを変更して…というのは非効率
    # 普通に選ぶ・選ばないで2^n

    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    n2 = 1 << N  # 左シフト i.e. n2 = 2^n
    for t in range(n2):
        d = {}  # 辞書に文字と出現回数をセットにして格納
        for i in range(N):
            # <bit全探索>
            # t(カウント)を選ぶ・選ばないを判断したい桁数分右シフト
            # i.e. 末尾の桁を消す
            # カウントをi回右にシフトして1と論理積を取る
            # i.e. 最下位の桁が1かどうかチェックする
            if (t >> i) & 1:
                # 文字列に含まれるアルファベットを辞書に格納
                for s in S[i]:
                    if s in d:
                        d[s] += 1
                    else:
                        d[s] = 1
        cnt = 0  # 出現回数がkだった文字の個数をカウント
        for k, v in d.items():
            if v == K:
                cnt += 1
        ans = max(ans, cnt)

    print(ans)


main()
