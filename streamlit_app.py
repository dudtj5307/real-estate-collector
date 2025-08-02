import streamlit as st
import main

st.set_page_config(page_title="네이버 부동산 검색", page_icon="🏠", layout="centered", initial_sidebar_state="auto")
st.title("🏠 네이버 부동산 검색")

# Select location
st.write("")
st.write("검색하고자 하는 지역을 선택하세요.")

if 'clicked_city' not in st.session_state:
    st.session_state.clicked_city = None
if 'clicked_dist' not in st.session_state:
    st.session_state.clicked_dist = None
if 'clicked_town' not in st.session_state:
    st.session_state.clicked_town = None


def update_buttons():
    pass

def reload_city():
    city_data = main.get_list_city()
    city_col = st.columns(len(city_data), gap="small", vertical_alignment="top")
    for i, city_name in enumerate(city_data.keys()):
        with city_col[i]:
            if st.button(f"{city_name}", key=f"dist_btn_{city_name}"):
                st.session_state.clicked_city = city_name
                st.session_state.clicked_dist = None
                st.session_state.clicked_town = None

    if st.session_state.clicked_city:
        reload_district(city_data[st.session_state.clicked_city])

def reload_district(cityNo):
    dist_data = main.get_list_district(cityNo)
    dist_col = st.columns(len(dist_data), gap="medium", vertical_alignment="top")
    for i, dist_name in enumerate(dist_data.keys()):
        with dist_col[i]:
            if st.button(f'{dist_name}'):
                st.session_state.clicked_dist = dist_name
                st.session_state.clicked_town = None

    if st.session_state.clicked_dist:
        reload_town(dist_data[st.session_state.clicked_dist])


def reload_town(distNo):
    town_data = main.get_list_town(distNo)
    town_col = st.columns(len(town_data), gap="medium", vertical_alignment="top")
    for i, town_name in enumerate(town_data.keys()):
        with town_col[i]:
            if st.button(f'{town_name}'):
                st.session_state.clicked_town = town_name

    if st.session_state.clicked_town:
        st.write(f'{st.session_state.clicked_town}')




if __name__ == '__main__':
    reload_city()