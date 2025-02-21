import streamlit as st
import statistics
import math
import matplotlib.pyplot as plt

def calculate_brendan_score_qb(players):
    max_class = 4

    list_of_overalls = []
    list_of_classes = []
    list_of_bscores = []
    num_of_players = 0
    for i in players:
        list_of_overalls.append(i[0])
        list_of_classes.append(i[1])
        num_of_players+=1
    overall_mean = statistics.mean(list_of_overalls)
    # print("overall mean: ", overall_mean)
    overall_std = statistics.stdev(list_of_overalls)
    # print(f'overall std: {overall_std}')
    class_mean = statistics.mean(list_of_classes)
    class_std = statistics.stdev(list_of_classes)


    for i in players:
        player_overall = i[0]
        numerator = player_overall - overall_mean
        denominator = overall_std / math.sqrt(num_of_players)
        standardized_overall = numerator / denominator

        player_class = i[1]
        numerator = (max_class - player_class) - class_mean
        denominator = class_std / math.sqrt(num_of_players)
        print(f'numerator: {numerator} / {denominator}')
        if denominator != 0:

            standardized_class = numerator / denominator
        else:
            standardized_class = 0
        print(f'standard_overall: {standardized_overall * 0.65} + {standardized_class * 0.35}')
        final_player_score = (standardized_overall * 0.65) + (standardized_class * 0.35)
        list_of_bscores.append(round(final_player_score,2))
        # list_of_bscores.append(final_player_score)
        # return round(final_player_score,2)



    # print(list_of_overalls)
    # print(list_of_classes)
    print(f'B-scores: {list_of_bscores}')
    print(f'Avg b-score for this set is: {statistics.mean(list_of_bscores)}')

    print(f'There are {num_of_players} players in this set!')
    return statistics.mean(list_of_bscores)




st.title("📊 B-Score Graph")
st.write("Here is the B-Score graph visualization.")

list_of_avg_b_scores = []
# qb_tuple = ((86, 2), (81, 1), (77, 1), (77,1), (71, 1)) #ohio bobcats
# qb_tuple = ((85, 3), (78,2),(74,2), (71,1)) #Minnesota
qb_tuple = st.session_state['qb']
print("---------qb scores -----------")
if len(qb_tuple) > 1:

    result = calculate_brendan_score_qb(qb_tuple)
    list_of_avg_b_scores.append(("qb",result))


print("---------rb scores -------------")
# rb_tuple = ((90, 3), (86, 3), (74, 1), (69, 1), (62, 1)) #ohio bobacats
# rb_tuple = ((93,4),(78,1), (76,2), (75,2), (66,1), (66,1)) #Minnestota

rb_tuple = st.session_state['rb']
if len(rb_tuple) > 1:

    result = calculate_brendan_score_qb(rb_tuple)
    list_of_avg_b_scores.append(("rb",result))

print("--------wr scores--------------")
# wr_tuple = ((86,3), (86,4), (84, 2), (84, 1), (83,3), (81,2), (80,3), (78, 2), (77,1), (62,1)) #ohio bobacats
# wr_tuple = ((84,4),(82,3), (80,3),(80,2),(74,3),(74,1),(73,2),(65,2), (64,1)) #Minnestota
wr_tuple = st.session_state['wr']
if len(wr_tuple) > 1:

    result = calculate_brendan_score_qb(wr_tuple)
    list_of_avg_b_scores.append(("wr",result))

print("-------te scores ------------")
# te_tuple = ((87, 4), (86,3), (80, 1), (76, 1)) #ohio bobacats
# te_tuple = ((90,2), (79,2), (78,2), (75,2)) #Minnestota
te_tuple = st.session_state['te']
if len(te_tuple) > 1:

    result = calculate_brendan_score_qb(te_tuple)
    list_of_avg_b_scores.append(("te",result))

print("-------lt scores ------------")
lt_tuple = ((90,4), (79,1), (78,1))
result = calculate_brendan_score_qb(lt_tuple) #ohio bobacats
# list_of_avg_b_scores.append(("lt",result))

print("-------lg scores -----------")
lg_tuple = ((90,4), (81,1), (80,1))
result = calculate_brendan_score_qb(lg_tuple) #ohio bobacats
# list_of_avg_b_scores.append(("lg", result))

print("--------c scores -----------")
c_tuple = ((88,3), (82,2), (73,2), (71,1)) #ohio bobacats
result = calculate_brendan_score_qb(c_tuple)
# list_of_avg_b_scores.append(("c", result))

print("--------rg scores -----------")
rg_tuple = ((95,4), (91,3))
result = calculate_brendan_score_qb(rg_tuple) #ohio bobacats
# list_of_avg_b_scores.append(("rg", result))

print("--------rt scores -----------")
rt_tuple = ((90, 3), (87, 3), (80,1), (78,1)) #ohio bobacats
result = calculate_brendan_score_qb(rt_tuple)
# list_of_avg_b_scores.append(("rt", result))

print("---------g scores -----------")
# g_tuple = ((90,4), (79,1), (78,1),(90,4), (81,1), (80,1),(88,3), (82,2), (73,2), (71,1), (95,4), (91,3), (90, 3), (87, 3), (80,1), (78,1)) #ohio bobacats
# g_tuple = ((81,2), (75,1), (70,1), (87,2), (68,1), (85,4), (75,1), (74,1), (87,3),(84,4),(80,1), (78,3), (76,1), (76,2), (72,1), (61,1), (78,2), (69,1), (69,1), (68,1), (67,1)) # Minnesota
g_tuple = st.session_state['g']
if len(g_tuple) > 1:

    result = calculate_brendan_score_qb(g_tuple)
    list_of_avg_b_scores.append(("g", result))

print("--------le scores -----------")
le_tuple = ((94,4), (93,3), (86,3), (84,1))
result = calculate_brendan_score_qb(le_tuple)
# list_of_avg_b_scores.append(("le", result))

print("--------re scores -----------")
re_tuple = ((86, 3), (74,2))
result = calculate_brendan_score_qb(re_tuple)
# list_of_avg_b_scores.append(("re", result))

print("---------- de scores ---------")
# de_tuple = ((94,4), (93,3), (86,3), (84,1), (86, 3), (74,2)) #ohio bobacats
# de_tuple = ((85,4), (82,4), (79,2),(87,2), (70,1), (69,1), (69,1)) # Minnesota
de_tuple = st.session_state['de']
if len(de_tuple) > 1:

    result = calculate_brendan_score_qb(de_tuple)
    list_of_avg_b_scores.append(("de", result))

print("--------dt scores -----------")
# dt_tuple = ((89,3), (87,2), (82,1), (82,1), (76,3), (75,1), (73,1)) #ohio bobacats
# dt_tuple = ((77,4), (70,1), (69,2), (66,1)) # Minnesota
dt_tuple = st.session_state['dt']
if len(dt_tuple) > 1:

    result = calculate_brendan_score_qb(dt_tuple)
    list_of_avg_b_scores.append(("dt", result))

print("--------olb scores -----------")
# olb_tuple = ((86,3), (82,1), (91,4), (80,1), (77,1)) #ohio bobacats
# olb_tuple = ((80,4), (78,2),(81,4),(76,4), (72,2), (69,1)) # Minnesota
olb_tuple = st.session_state['olb']
if len(olb_tuple) > 1:

    result = calculate_brendan_score_qb(olb_tuple)
    list_of_avg_b_scores.append(("olb", result))

print("--------mlb scores -----------")
# mlb_tuple = ((88, 2), (85,3), (80,1), (77,1)) #ohio bobacats
# mlb_tuple = ((86,3), (79,2), (71,1), (68,3), (66,3)) #Minnesota
mlb_tuple = st.session_state['mlb']
if len(mlb_tuple) > 1:

    result = calculate_brendan_score_qb(mlb_tuple)
    list_of_avg_b_scores.append(("mlb", result))

print("--------cb scores -----------")
# cb_tuple = ((91,3), (90,4), (90,2), (89,4), (86,2), (85,2), (84,2), (82,4), (80,1), (78,1), (72,1), (70,1)) #ohio bobacats
# cb_tuple = ((87,3),(85,2), (84,4), (82,4), (77,2), (76,1), (74,1), (73,1), (70,1)) #Minnesota
cb_tuple = st.session_state['cb']
if len(cb_tuple) > 1:

    result = calculate_brendan_score_qb(cb_tuple)
    list_of_avg_b_scores.append(("cb", result))

print("--------fs scores -----------")
# fs_tuple = ((85,4), (82,2), (81,1), (75,1), (71,3)) #ohio bobacats
# fs_tuple = ((86,1), (83,3), (75,2), (59,1)) #Minnesota
fs_tuple = st.session_state['fs']
if len(fs_tuple) > 1:

    result = calculate_brendan_score_qb(fs_tuple)
    list_of_avg_b_scores.append(("fs", result))

print("--------ss scores -----------")
# ss_tuple = ((82,2), (77,2), (77,1)) #ohio bobacats
# ss_tuple = ((83,3), (78, 3), (69,1)) #Minnesota
ss_tuple = st.session_state['ss']
if len(ss_tuple) > 1:

    result = calculate_brendan_score_qb(ss_tuple)
    list_of_avg_b_scores.append(("ss", result))

print(f'list of average_bscores: {list_of_avg_b_scores}')
list_of_positions = []
list_of_b_scores_single = []
for i in list_of_avg_b_scores:
    list_of_positions.append(i[0])
    list_of_b_scores_single.append(i[1])


fig, ax = plt.subplots()


plt.bar(list_of_positions,list_of_b_scores_single, color=['red', 'blue', 'orange', 'purple'])
plt.xlabel("Position")
plt.ylabel("B-Score")
plt.title("Avg B-score by position")
plt.show()

print(f'state on graph page: {st.session_state}')

st.pyplot(fig)