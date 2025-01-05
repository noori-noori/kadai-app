import streamlit as st

st.title("課題アプリ: 占い診断Webアプリ")
st.write("### あなたの人となりを診断しましょう")
st.write("##### A:画数")
st.write("お名前を入力して占う")
st.write("##### B:数秘")
st.write("誕生日を入力して占う")

selected_item = st.radio(
    "選択してください。",
    ["A:画数", "B:数秘"]
)

st.divider()

if selected_item == "A:画数":
    name = st.text_input(label="お名前をひらがなで入力してください。")
    name_count = len(name)
else:
    birthday = st.text_input(label="お誕生日を西暦から8桁で入力してください。ex.20250101")
    bd_count = sum([int(i) for i in birthday])

if st.button("占う"):
    st.divider()
    if selected_item == "A:画数":
        if name:
            st.write(f"**{name_count}**")
        else:
            st.error("対象となるお名前をひらがな入力してから「占う」ボタンを押してください。")
    else:
        if birthday:
                st.write(f"**{bd_count}**")
        else:
            st.error("お誕生日を西暦から8桁で入力してください。")