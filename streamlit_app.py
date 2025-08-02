import streamlit as st
import main

st.set_page_config(page_title="네이버 부동산 검색", page_icon="🏠", layout="wide", initial_sidebar_state="auto")
st.markdown(
    "<h1 style='font-size:40px;'>🏠 네이버 부동산 검색</h1>",
    unsafe_allow_html=True
)

# Select location
st.write("")
st.write("검색하고자 하는 지역을 선택하세요.")

stState = st.session_state
if 'selected_city' not in stState:
    stState.selected_city = None
if 'selected_dist' not in stState:
    stState.selected_dist = None
if 'selected_town' not in stState:
    stState.selected_town = None
if 'disabled' not in stState:
    stState.disabled_dist = True
    stState.disabled_town = True


st.markdown("""
<style>
div[data-testid="stHorizontalBlock"][class*="st-emotion-cache"] {
    flex-wrap: wrap !important;
}
</style>
""", unsafe_allow_html=True)

def update_buttons():
    pass

def reload_city():
    city_data = main.get_list_city()
    selected_city = st.selectbox("시/도", city_data.keys(),
                                 index=None,
                                 placeholder="시/도를 선택하세요",)
    if selected_city:
        stState.selected_city = selected_city
        stState.selected_dist = None
        stState.selected_town = None
        stState.disabled_dist = False
        reload_district(city_data[selected_city])
    else:
        reload_district({})


def reload_district(cityNo):
    dist_data = main.get_list_district(cityNo)
    selected_dist = st.selectbox("시/구/군", dist_data.keys(),
                                 index=None,
                                 placeholder="시/구/군을 선택하세요",
                                 disabled=stState.disabled_dist,)

    if selected_dist:
        stState.selected_dist = selected_dist
        stState.selected_town = None
        stState.disabled_town = False
        reload_town(dist_data[selected_dist])
    else:
        reload_town({})

def reload_town(distNo):
    # town_data = {'전체':'All'} | main.get_list_town(distNo)
    # selected_town = st.selectbox("시/구/군", town_data.keys(),
    #                              index=0,
    #                              disabled=stState.disabled_town,)

    town_data = main.get_list_town(distNo)
    selected_town = st.multiselect("시/구/군",
                                   options=town_data.keys(),
                                   default=town_data.keys(),
                                   disabled=stState.disabled_town,)


    # if selected_town:
    #     stState.selected_town = selected_town
    #     st.write(f'{stState.selected_city} {stState.selected_dist} {stState.selected_town}')
    #
    #     reload_apartment(town_data[selected_town])
    #
    # else:
    #     reload_district({})


def reload_apartment(townNo):
    apart_data = main.get_list_apartment(townNo)
    # st.write(apart_data.keys())
    pass

if __name__ == '__main__':
    reload_city()