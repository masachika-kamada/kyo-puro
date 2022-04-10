import streamlit as st


def main():
    st.markdown('# 競プロサポーター')
    st.markdown('## 数値index')
    vals = st.text_input('数値indexチェッカー')
    if vals:
        vals = list(map(int, vals.split()))
        sorted_vals = sorted(vals)
        dst = []
        for val in vals:
            dst.append(sorted_vals.index(val))

        st.markdown(f'#### {dst} ')


if __name__ == '__main__':
    main()
