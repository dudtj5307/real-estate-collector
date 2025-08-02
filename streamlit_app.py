import time

import streamlit as st
import main

st.set_page_config(page_title="네이버 부동산 검색", page_icon="🏠", layout="wide", initial_sidebar_state="auto")
st.markdown(
    "<h1 style='font-size:35px;'>🏠 네이버 부동산 검색</h1>",
    unsafe_allow_html=True
)

# Select location
stState = st.session_state
if 'selected_city' not in stState:
    stState.selected_city = None
if 'selected_dist' not in stState:
    stState.selected_dist = None
if 'selected_town' not in stState:
    stState.selected_towns = []
    stState.town_name2no = {}
if 'disabled' not in stState:
    stState.disabled_dist = True
    stState.disabled_town = True

if "search_clicked" not in stState:
    stState.search_clicked = False

def update_buttons():
    pass

def reload_city():
    city_data = main.get_list_city()
    selected_city = st.selectbox("시/도", city_data.keys(), index=None,
                                 placeholder="시/도를 선택하세요",)
    stState.selected_city = selected_city
    if selected_city:
        stState.selected_dist = None
        stState.selected_town = None
        stState.disabled_dist = False
        stState.disabled_town = False
        reload_district(city_data[selected_city])

def reload_district(cityNo):
    dist_data = main.get_list_district(cityNo)
    selected_dist = st.selectbox("시/구/군", dist_data.keys(), index=None,
                                 placeholder="시/구/군을 선택하세요",
                                 disabled=stState.disabled_dist,)
    stState.selected_dist = selected_dist

    stState.selected_town = None
    if selected_dist:
        stState.disabled_town = False
        reload_town(dist_data[selected_dist])

def reload_town(distNo):
    town_name2no = main.get_list_town(distNo)
    stState.town_name2no = town_name2no

    selected_towns = st.multiselect("읍/면/동", options=town_name2no.keys(),
                                   default=town_name2no.keys(),
                                   placeholder="읍/면/동을 선택하세요",
                                   disabled=stState.disabled_town,)
    stState.selected_towns = selected_towns
    if selected_towns:
        set_checkboxes()
        set_searchButton()

def get_complex_datas(cortarNames):
    datas = {}
    for cortarName in cortarNames:
        cortarNo = stState.town_name2no[cortarName]
        complex_name2no = main.get_list_complex(cortarNo)

        datas[cortarName] = complex_name2no
        # for key, val in complex_name2no.items():
        #     datas[cortarName][key] = main.get_list_products(val)

    return datas

def set_checkboxes():
    urgent_sell = st.checkbox('급매', value=True, disabled=True)


def set_searchButton():
    if not stState.search_clicked:
        search_button = st.button("🔎 검색", use_container_width=True, key="search_button")
        if search_button:
            stState.search_result = []
            run_search()

def run_search():
    if not stState.selected_towns:
        st.write('해당 구역에는 아파트가 없습니다..!')
        return

    cortarNames = [name for name in stState.selected_towns]
    complex_datas = get_complex_datas(cortarNames)


    st.write(complex_datas)



if __name__ == '__main__':
    reload_city()