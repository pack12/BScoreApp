import streamlit as st

st.title("➕ Add Player")
st.write("This is the page to add a player.")
st.markdown("""
    <style>
        .button-container {
            display: flex;
            align-items: center;  /* Align vertically */
            height: 27px;  /* Match input field height */
        }
        
       .remove {
       display: flex;
       align-items: center;
       height: 10px;}
    </style>
""", unsafe_allow_html=True)

# qb, rb, wr, te, ol = st.columns(5, vertical_alignment="center")
selected_position = st.selectbox("Choose an option", ["QB", "RB", "WR", "TE", "G", "DT", "DE", "OLB", "MLB", "CB", "FS", "SS"])
selected_position_lower = selected_position.lower()
player_rating, player_class, add_button = st.columns(3)

rating = player_rating.number_input("Enter player rating", min_value=0, max_value=99)
player_c = player_class.selectbox("Select class", ["Freshman", "Sophomore", "Junior", "Senior"])

if 'qb' not in st.session_state:
    st.session_state['qb'] = []
if 'rb' not in st.session_state:
    st.session_state['rb'] = []
if 'wr' not in st.session_state:
    st.session_state['wr'] = []
if 'te' not in st.session_state:
    st.session_state['te'] = []
if 'g' not in st.session_state:
    st.session_state['g'] = []
if 'de' not in st.session_state:
    st.session_state['de'] = []
if 'dt' not in st.session_state:
    st.session_state['dt'] = []
if 'olb' not in st.session_state:
    st.session_state['olb'] = []
if 'mlb' not in st.session_state:
    st.session_state['mlb'] = []
if 'cb' not in st.session_state:
    st.session_state['cb'] = []
if 'fs' not in st.session_state:
    st.session_state['fs'] = []
if 'ss' not in st.session_state:
    st.session_state['ss'] = []
if 'remove' not in st.session_state:
    st.session_state['remove'] = []


# add_button.button("Add Player")
# Add spacing before the button
def convert_class_num(class_str):
    if class_str == 'Freshman':
        return 1
    elif class_str == 'Sophomore':
        return 2
    elif class_str == 'Junior':
        return 3
    elif class_str == 'Senior':
        return 4

def convert_from_num_to_class(class_num):
    if class_num == 1:
        return 'Freshman'
    elif class_num == 2:
        return 'Sophomore'
    elif class_num == 3:
        return 'Junior'
    elif class_num == 4:
        return 'Senior'

def add_player():
    class_num = convert_class_num(player_c)
    st.session_state[selected_position_lower].append((rating,class_num))

def remove_player(index):
    st.session_state[selected_position_lower].pop(index)
    print(st.session_state[selected_position_lower])

with add_button:
    st.markdown('<div class="button-container align-right">', unsafe_allow_html=True)
    st.button("" ,on_click=add_player, key='add_btn',icon=":material/add:")
    st.markdown('</div>', unsafe_allow_html=True)

    print(st.session_state[selected_position_lower])


st.subheader(f'{selected_position}s')
for i in range(len(st.session_state[selected_position_lower])):

    player_label, remove_btn = st.columns([1,2])
    with player_label:
        class_str = convert_from_num_to_class(st.session_state[selected_position_lower][i][1])
        st.write(f'Rating: {st.session_state[selected_position_lower][i][0]} \t Class: {class_str}')

    button_key = f'remove_button_{i}'
    with remove_btn:
        # st.markdown('<div class="remove">', unsafe_allow_html=True)
        if st.button("Remove Player",key=button_key):
            # st.markdown('</div>', unsafe_allow_html=True)
            remove_player(i)

            st.session_state[selected_position_lower] = st.session_state[selected_position_lower]
            print(f'removing player: {i}')
            st.rerun()










