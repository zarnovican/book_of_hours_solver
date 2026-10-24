import streamlit as st


assert "skill" in st.session_state

st.header("skill")

skill_cols = (
    300,    # name
    140,    # level
    800,    # attributes
    100,    # edit
)
con_skill = st.container(gap="xxsmall", width=sum(skill_cols))
col_name, col_level, col_attributes, _ = con_skill.columns(skill_cols)
col_name.write("learned")
col_level.write("level")
col_attributes.write("attributes")

st.header("language")
language_cols = (
    200,    # name
    140,    # level
    550,    # attributes
    100,    # edit
)
con_language = st.container(gap="xxsmall", width=sum(language_cols))
_, col_level, col_attributes, _ = con_language.columns(language_cols)
col_level.write("level")
col_attributes.write("attributes")

for item in st.session_state.skill:
    if item.is_language:
        col_enable, col_level, col_attributes, col_edit = con_language.columns(language_cols, vertical_alignment="center")
    else:
        col_enable, col_level, col_attributes, col_edit = con_skill.columns(skill_cols, vertical_alignment="center")

    if col_enable.checkbox(item.name, value=item.enable, on_change=item.update, key=item.enable_key):
        col_level.number_input("level", min_value=1, max_value=9, value=item.level, on_change=item.update, label_visibility="collapsed", key=item.level_key)

        with col_edit.popover("edit", icon=":material/edit:"):
            st.number_input("level cap", value=item.level_cap, min_value=1, max_value=9, on_change=item.update, key=item.level_cap_key)
            st.selectbox("committed to", index=item.valid_wisdoms.index(item.committed_to), options=item.valid_wisdoms, on_change=item.update, key=item.committed_to_key)
            st.checkbox("fulfilled", disabled=not bool(item.committed_to), value=item.fulfilled, on_change=item.update, key=item.fulfilled_key)

        col_attributes.write(item.attributes)
    else:
        col_level.space(size="medium")
