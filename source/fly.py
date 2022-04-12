import os
import airsim
import pickle
import pprint

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
#                 "/../path_planning/")

from path_planning.Dijkstra import Dijkstra
from path_planning.plotting import Plotting
from path_planning.multiple_stop_sequence_planner import tsp

def endSession(reset=True):
    if reset:
        client.reset()
        client.armDisarm(False)

    # that's enough fun for now. let's quit cleanly
    client.enableApiControl(False)

# _WAY_POINTS = [[0, 0, -30], [15, 15, -30], [20, 15, -30], [20, 20, -30], [25, 25, -30], [40, -30, -30], [45, 40, -30], [50, 50, -30], [50, 50, -5]]
# _TEST_DIJKSTRA_WAYPOINT_LISTS = [(900, 925), (901, 924), (902, 923), (903, 922), (904, 921), (905, 920), (906, 919), (907, 918), (908, 917), (909, 916), (910, 915), (911, 914), (912, 913), (913, 912), (914, 911), (915, 910), (916, 909), (917, 908), (918, 907), (919, 906), (920, 905), (921, 904), (922, 903), (923, 902), (924, 901), (925, 900), (926, 899), (927, 898), (928, 897), (929, 896), (930, 895), (931, 894), (932, 893), (933, 892), (934, 891), (935, 890), (936, 889), (937, 888), (938, 887), (939, 886), (940, 885), (941, 884), (942, 883), (943, 882), (944, 881), (945, 880), (946, 879), (947, 878), (948, 877), (949, 876), (950, 875), (951, 874), (952, 873), (953, 872), (954, 871), (955, 870), (956, 869), (957, 868), (958, 867), (959, 866), (960, 865), (961, 864), (962, 863), (963, 862), (964, 861), (965, 860), (966, 859), (967, 858), (967, 857), (967, 856), (967, 855), (967, 854), (967, 853), (967, 852), (967, 851), (967, 850), (967, 849), (967, 848), (967, 847), (967, 846), (967, 845), (967, 844), (967, 843), (967, 842), (967, 841), (967, 840), (967, 839), (967, 838), (967, 837), (967, 836), (967, 835), (967, 834), (967, 833), (967, 832), (967, 831), (967, 830), (967, 829), (967, 828), (967, 827), (967, 826), (967, 825), (967, 824), (967, 823), (967, 822), (967, 821), (967, 820), (967, 819), (967, 818), (967, 817), (967, 816), (967, 815), (967, 814), (967, 813), (967, 812), (967, 811), (967, 810), (967, 809), (967, 808), (967, 807), (967, 806), (967, 805), (967, 804), (967, 803), (967, 802), (967, 801), (967, 800), (967, 799), (967, 798), (967, 797), (967, 796), (967, 795), (967, 794), (967, 793), (967, 792), (967, 791), (967, 790), (967, 789), (967, 788), (967, 787), (967, 786), (967, 785), (967, 784), (967, 783), (967, 782), (967, 781), (967, 780), (967, 779), (967, 778), (967, 777), (967, 776), (967, 775), (967, 774), (967, 773), (967, 772), (967, 771), (967, 770), (967, 769), (967, 768), (967, 767), (967, 766), (967, 765), (967, 764), (967, 763), (967, 762), (967, 761), (967, 760), (967, 759), (967, 758), (967, 757), (967, 756), (967, 755), (967, 754), (967, 753), (967, 752), (967, 751), (967, 750), (967, 749), (967, 748), (967, 747), (967, 746), (967, 745), (967, 744), (967, 743), (967, 742), (967, 741), (967, 740), (967, 739), (967, 738), (967, 737), (967, 736), (967, 735), (967, 734), (967, 733), (967, 732), (967, 731), (967, 730), (967, 729), (967, 728), (967, 727), (967, 726), (967, 725), (967, 724), (967, 723), (967, 722), (967, 721), (967, 720), (967, 719), (967, 718), (967, 717), (967, 716), (967, 715), (967, 714), (967, 713), (967, 712), (967, 711), (967, 710), (967, 709), (967, 708), (967, 707), (967, 706), (967, 705), (967, 704), (967, 703), (966, 702), (965, 701), (964, 700), (963, 699), (962, 698), (961, 697), (960, 696), (959, 695), (958, 694), (957, 693), (956, 692), (955, 691), (954, 690), (953, 689), (952, 688), (951, 687), (950, 686), (949, 685), (948, 684), (947, 683), (946, 682), (945, 681), (944, 680), (943, 679), (942, 678), (941, 677), (940, 676), (939, 675), (938, 674), (938, 673), (938, 672), (938, 671), (938, 670), (938, 669), (938, 668), (938, 667), (938, 666), (938, 665), (938, 664), (938, 663), (938, 662), (938, 661), (938, 660), (938, 659), (938, 658), (938, 657), (938, 656), (938, 655), (938, 654), (938, 653), (938, 652), (938, 651), (938, 650), (938, 649), (938, 648), (938, 647), (938, 646), (938, 645), (938, 644), (938, 643), (938, 642), (938, 641), (938, 640), (938, 639), (938, 638), (938, 637), (938, 636), (938, 635), (938, 634), (938, 633), (938, 632), (938, 631), (938, 630), (938, 629), (938, 628), (938, 627), (938, 626), (938, 625), (938, 624), (938, 623), (938, 622), (938, 621), (938, 620), (938, 619), (938, 618), (938, 617), (938, 616), (938, 615), (938, 614), (938, 613), (938, 612), (938, 611), (938, 610), (938, 609), (938, 608), (938, 607), (938, 606), (938, 605), (938, 604), (938, 603), (938, 602), (938, 601), (938, 600), (938, 599), (937, 598), (936, 597), (935, 596), (934, 595), (934, 594), (934, 593), (934, 592), (934, 591), (933, 590), (932, 589), (931, 588), (930, 587), (929, 586), (928, 585), (927, 584), (926, 583), (925, 582), (924, 581), (923, 580), (922, 579), (921, 578), (920, 577), (919, 576), (918, 575), (917, 574), (916, 573), (915, 572), (914, 571), (913, 570), (912, 569), (911, 568), (910, 567), (909, 566), (908, 565), (907, 564), (906, 563), (905, 562), (904, 561), (903, 560), (902, 559), (901, 558), (900, 557), (899, 556), (898, 555), (897, 554), (896, 553), (895, 552), (894, 551), (893, 550), (892, 549), (891, 548), (890, 547), (889, 546), (888, 545), (887, 544), (886, 543), (885, 542), (884, 541), (883, 540), (882, 539), (881, 538), (880, 537), (879, 536), (878, 535), (877, 534), (876, 533), (875, 532), (874, 531), (873, 530), (872, 529), (871, 528), (870, 527), (869, 526), (868, 525), (867, 524), (866, 523), (865, 522), (864, 521), (863, 520), (862, 519), (861, 518), (860, 517), (859, 516), (858, 515), (857, 514), (856, 513), (855, 512), (854, 511), (853, 511), (852, 511), (851, 511), (850, 511), (849, 511), (848, 511), (847, 511), (846, 511), (845, 511), (844, 511), (843, 511), (842, 511), (841, 511), (840, 511), (839, 511), (838, 511), (837, 511), (836, 511), (835, 511), (834, 511), (833, 511), (832, 511), (831, 511), (830, 511), (829, 511), (828, 511), (827, 511), (826, 511), (825, 511), (824, 511), (823, 511), (822, 511), (821, 511), (820, 511), (819, 511), (818, 511), (817, 511), (816, 511), (815, 511), (814, 511), (813, 511), (812, 511), (811, 511), (810, 511), (809, 511), (808, 511), (807, 511), (806, 511), (805, 511), (804, 511), (803, 511), (802, 511), (801, 511), (800, 511), (799, 511), (798, 511), (797, 511), (796, 511), (795, 511), (794, 511), (793, 511), (792, 511), (791, 511), (790, 511), (789, 511), (788, 511), (787, 511), (786, 511), (785, 511), (784, 511), (783, 511), (782, 511), (781, 511), (780, 511), (779, 511), (778, 511), (777, 511), (776, 511), (775, 511), (774, 511), (773, 511), (772, 511), (771, 511), (770, 511), (769, 511), (768, 511), (767, 511), (766, 511), (765, 511), (764, 511), (763, 511), (762, 511), (761, 511), (760, 511), (759, 511), (758, 511), (757, 511), (756, 511), (755, 511), (754, 511), (753, 511), (752, 511), (751, 510), (750, 510), (749, 510), (748, 510), (747, 510), (746, 510), (745, 510), (744, 510), (743, 510), (742, 510), (741, 510), (740, 510), (739, 510), (738, 510), (737, 510), (736, 510), (735, 510), (734, 510), (733, 510), (732, 510), (731, 510), (730, 510), (729, 510), (728, 510), (727, 510), (726, 510), (725, 510), (724, 510), (723, 510), (722, 510), (721, 510), (720, 510), (719, 510), (718, 510), (717, 510), (716, 510), (715, 510), (714, 510), (713, 510), (712, 510), (711, 510), (710, 510), (709, 510), (708, 510), (707, 510), (706, 510), (705, 510), (704, 510), (703, 510), (702, 510), (701, 510), (700, 510), (699, 510), (698, 510), (697, 510), (696, 510), (695, 510), (694, 510), (693, 510), (692, 510), (691, 510), (690, 510), (689, 510), (688, 510), (687, 510), (686, 510), (685, 510), (684, 510), (683, 510), (682, 510), (681, 510), (680, 510), (679, 510), (678, 510), (677, 510), (676, 510), (675, 510), (674, 510), (673, 510), (672, 510), (671, 510), (670, 510), (669, 510), (668, 510), (667, 510), (666, 510), (665, 510), (664, 510), (663, 510), (662, 510), (661, 510), (660, 510), (659, 510), (658, 510), (657, 510), (656, 510), (655, 510), (654, 510), (653, 510), (652, 510), (651, 510), (650, 510), (649, 510), (648, 510), (647, 510), (646, 510), (645, 510), (644, 510), (643, 510), (642, 510), (641, 510), (640, 510), (639, 510), (638, 510), (637, 510), (636, 510), (635, 510), (634, 510), (633, 510), (632, 510), (631, 510), (630, 510), (629, 510), (628, 510), (627, 510), (626, 510), (625, 510), (624, 509), (623, 508), (622, 507), (621, 506), (620, 505), (619, 505), (618, 505), (617, 505), (616, 505), (615, 505), (614, 505), (613, 505), (612, 505), (611, 505), (610, 505), (609, 505), (608, 505), (607, 505), (606, 505), (605, 505), (604, 505), (603, 505), (602, 505), (601, 505), (600, 505), (599, 504), (598, 503), (597, 502), (596, 501), (595, 500), (594, 500), (593, 500), (592, 500), (591, 500), (590, 500), (589, 500), (588, 500), (587, 500), (586, 500), (585, 500), (584, 500), (583, 500), (582, 500), (581, 500), (580, 500), (579, 500), (578, 500), (577, 500), (576, 500), (575, 500), (574, 500), (573, 500), (572, 500), (571, 500), (570, 500), (569, 500), (568, 500), (567, 500), (566, 500), (565, 500), (564, 500), (563, 500), (562, 500), (561, 500), (560, 500), (559, 500), (558, 500), (557, 500), (556, 500), (555, 500), (554, 500), (553, 500), (552, 500), (551, 500), (550, 500), (549, 500), (548, 500), (547, 500), (546, 500), (545, 500), (544, 500), (543, 500), (542, 500), (541, 500), (540, 500), (539, 500), (538, 500), (537, 500), (536, 500), (535, 500), (534, 500), (533, 500), (532, 500), (531, 500), (530, 500), (529, 500), (528, 500), (527, 500), (526, 500), (525, 500), (524, 500), (523, 500), (522, 500), (521, 500), (520, 500), (519, 500), (518, 500), (517, 500), (516, 500), (515, 500), (514, 500), (513, 500), (512, 500), (511, 500), (510, 500), (509, 500), (508, 500), (507, 500), (506, 500), (505, 500), (504, 500), (503, 500), (502, 500), (501, 500), (500, 500)]
# _TEST_DIJKSTRA_WAYPOINT_LISTS = [[(625, 510), (624, 509), (623, 508), (622, 507), (621, 506), (620, 505), (619, 504), (618, 503), (617, 502), (616, 501), (615, 500), (614, 500), (613, 500), (612, 500), (611, 500), (610, 500), (609, 500), (608, 500), (607, 500), (606, 500), (605, 500), (604, 500), (603, 500), (602, 500), (601, 500), (600, 500), (599, 500), (598, 500), (597, 500), (596, 500), (595, 500), (594, 500), (593, 500), (592, 500), (591, 500), (590, 500), (589, 500), (588, 500), (587, 500), (586, 500), (585, 500), (584, 500), (583, 500), (582, 500), (581, 500), (580, 500), (579, 500), (578, 500), (577, 500), (576, 500), (575, 500), (574, 500), (573, 500), (572, 500), (571, 500), (570, 500), (569, 500), (568, 500), (567, 500), (566, 500), (565, 500), (564, 500), (563, 500), (562, 500), (561, 500), (560, 500), (559, 500), (558, 500), (557, 500), (556, 500), (555, 500), (554, 500), (553, 500), (552, 500), (551, 500), (550, 500), (549, 500), (548, 500), (547, 500), (546, 500), (545, 500), (544, 500), (543, 500), (542, 500), (541, 500), (540, 500), (539, 500), (538, 500), (537, 500), (536, 500), (535, 500), (534, 500), (533, 500), (532, 500), (531, 500), (530, 500), (529, 500), (528, 500), (527, 500), (526, 500), (525, 500), (524, 500), (523, 500), (522, 500), (521, 500), (520, 500), (519, 500), (518, 500), (517, 500), (516, 500), (515, 500), (514, 500), (513, 500), (512, 500), (511, 500), (510, 500), (509, 500), (508, 500), (507, 500), (506, 500), (505, 500), (504, 500), (503, 500), (502, 500), (501, 500), (500, 500)], [(500, 500), (501, 501), (502, 502), (503, 503), (504, 504), (505, 505), (506, 506), (507, 507), (508, 508), (509, 509), (510, 510), (511, 510), (512, 510), (513, 510), (514, 510), (515, 510), (516, 510), (517, 510), (518, 510), (519, 510), (520, 510), (521, 510), (522, 510), (523, 510), (524, 510), (525, 510), (526, 510), (527, 510), (528, 510), (529, 510), (530, 510), (531, 510), (532, 510), (533, 510), (534, 510), (535, 510), (536, 510), (537, 510), (538, 510), (539, 510), (540, 510), (541, 510), (542, 510), (543, 510), (544, 510), (545, 510), (546, 510), (547, 510), (548, 510), (549, 510), (550, 510), (551, 510), (552, 510), (553, 510), (554, 510), (555, 510), (556, 510), (557, 510), (558, 510), (559, 510), (560, 510), (561, 510), (562, 510), (563, 510), (564, 510), (565, 510), (566, 510), (567, 510), (568, 510), (569, 510), (570, 510), (571, 510), (572, 510), (573, 510), (574, 510), (575, 510), (576, 510), (577, 510), (578, 510), (579, 510), (580, 510), (581, 510), (582, 510), (583, 510), (584, 510), (585, 510), (586, 510), (587, 510), (588, 510), (589, 510), (590, 510), (591, 510), (592, 510), (593, 510), (594, 510), (595, 510), (596, 510), (597, 510), (598, 510), (599, 510), (600, 510), (601, 510), (602, 510), (603, 510), (604, 510), (605, 510), (606, 510), (607, 510), (608, 510), (609, 510), (610, 510), (611, 510), (612, 510), (613, 510), (614, 510), (615, 510), (616, 510), (617, 510), (618, 510), (619, 510), (620, 510), (621, 510), (622, 510), (623, 510), (624, 510), (625, 510)]]
_CORRECTION = 0
_PATHS_FILE_NAME = os.path.join(os.getcwd(), "teste_flight_paths.pickle")

_DESTINATIONS_TO_COORDS = {"Between the Traffic": (480, 450), "Into the Tree": (425, 400), "Concrete Plaza": (450, 710), "Brick Plaza": (350, 680)}
_S_START = (500, 500)
s_goals = [(480, 450), (425, 400), (450, 710), (350, 680)]#, (400, 425)]
# 1: between the cars, 2: into the tree, 3: empty concrete plaza, 4: brick plaza

# generate and save the path among all_destinations, to be looked up later
def generate_and_save_path_among(destinations: list):
    destinations.append(_S_START)
    l_destinations = len(destinations)
    paths = {}
    for i in range(l_destinations - 1):
        for j in range(i + 1, l_destinations):
            dijkstra = Dijkstra(destinations[i], destinations[j])
            curr_waypoints, visited = dijkstra.searching()
            paths[destinations[i] + destinations[j]] = {"curr_waypoints": curr_waypoints, "visited": visited}
            dijkstra = Dijkstra(destinations[j], destinations[i])
            curr_waypoints, visited = dijkstra.searching()
            paths[destinations[j] + destinations[i]] = {"curr_waypoints": curr_waypoints, "visited": visited}
    pickle.dump(paths, open(_PATHS_FILE_NAME,'wb'))
# generate_and_save_path_among(s_goals)

def export_map(client):
    print("exporting map")
    center = airsim.Vector3r(0, 0, 0)
    output_path = os.path.join(os.getcwd(), "source\\path_planning\\test_map_1000_1000_300.binvox")
    client.simCreateVoxelGrid(center, 1000, 1000, 200, 1, output_path)
    print("map exported")
# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.reset()
# export_map(client)

# generate path among the sequence of stops
# _TEST_DIJKSTRA_WAYPOINT_LISTS = []
# for i_stop in range(len(stop_sequence) - 1):
#     dijkstra = Dijkstra(s_goals[stop_sequence[i_stop]], s_goals[stop_sequence[i_stop + 1]])
#     curr_waypoints, visited = dijkstra.searching()
#     _TEST_DIJKSTRA_WAYPOINT_LISTS.append(curr_waypoints)
#     # plot = Plotting(s_goals[stop_sequence[i_stop]], s_goals[stop_sequence[i_stop + 1]])
#     # plot.animation(curr_waypoints, visited, "Dijkstra's")  # animation generate
# print("_TEST_DIJKSTRA_WAYPOINT_LISTS")
# print(_TEST_DIJKSTRA_WAYPOINT_LISTS)

client.enableApiControl(True)

state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)
# initial_location_xyz = state.position.x_val, state.position.y_val, state.position.z_val

imu_data = client.getImuData()
s = pprint.pformat(imu_data)
print("imu_data: %s" % s)

barometer_data = client.getBarometerData()
s = pprint.pformat(barometer_data)
print("barometer_data: %s" % s)

magnetometer_data = client.getMagnetometerData()
s = pprint.pformat(magnetometer_data)
print("magnetometer_data: %s" % s)

gps_data = client.getGpsData()
s = pprint.pformat(gps_data)
print("gps_data: %s" % s)

def takeoff():
    airsim.wait_key('Press any key to takeoff')
    print("Taking off...")
    client.armDisarm(True)
    client.takeoffAsync().join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

# airsim.wait_key('Press any key to move vehicle to the destination at 5 m/s')
# print("Flying...")
current_xy = 0, 0, -100
def fly(dijkstra_waypoint_lists):
    for waypoints in dijkstra_waypoint_lists:
        print("Start flying away from the starting point")
        i = 0
        for waypoint in reversed(waypoints):
            i += 1
            if i > 1 and i < len(waypoints) - 1:
                prev = waypoints[i - 2]
                curr = waypoints[i - 1]
                next = waypoints[i]
                if (curr[0] - prev[0] == next[0] - curr[0] and curr[1] - prev[1] == next[1] - curr[1]):
                    continue
            new_waypoint = (waypoint[1] - 500), (waypoint[0] + _CORRECTION - 500), -120
            yaw = 0
            yaw_mode = airsim.YawMode(is_rate=False, yaw_or_rate=yaw)
            move_future = client.moveToPositionAsync(new_waypoint[0], new_waypoint[1], new_waypoint[2], 10, drivetrain=airsim.DrivetrainType.ForwardOnly, yaw_mode=yaw_mode)
            while not move_future._set_flag:
                move_future._loop.start()
                distance_sensor_data = client.getDistanceSensorData()
                # dd = pprint.pformat(distance_sensor_data)
                # print("distance_sensor_data: %s" % dd)
                if (distance_sensor_data.distance < 20):
                    client.cancelLastTask()
                    client.hoverAsync().join()
                    exit()
            move_future.join()

            current_pose = client.simGetVehiclePose().position
            current_xy = current_pose.x_val, current_pose.y_val

        # Descend and hover for dropoff
        client.hoverAsync().join()
        client.moveToPositionAsync((waypoints[0][1] - 500), (waypoints[0][0] + _CORRECTION - 500), -5, 10).join()
        # state = client.getMultirotorState()
        # print("state: %s" % pprint.pformat(state))
        print("Arrived")

_PATHS_DICT = pickle.load(open(_PATHS_FILE_NAME,'rb'))
def try_flying_on_all_paths(curr_paths_dict):
    for k, v in curr_paths_dict.items():
        fly([v])
# try_flying_on_all_paths(_PATHS_DICT)

def fly_to_user_input(input_destinations):
    s_goals = []
    for dest in input_destinations:
        s_goals.append(_DESTINATIONS_TO_COORDS[dest])
    # Generate stop sequence, which is circular by nature
    s_goals.insert(0, _S_START)
    _, stop_sequence = tsp(s_goals)

    # rotate the stop sequence to start from _S_START
    stop_sequence = stop_sequence[:-1]
    i_start = stop_sequence.index(0)
    stop_sequence = stop_sequence[i_start:] + stop_sequence[:i_start] + [0]
    print("stop_sequence", stop_sequence)
    dijkstra_waypoint_list = []
    
    takeoff()
    for i_stop in range(len(stop_sequence) - 1):
        start_and_finish = s_goals[stop_sequence[i_stop]] + s_goals[stop_sequence[i_stop + 1]]
        curr_waypoints = None
        if start_and_finish in _PATHS_DICT:
            curr_waypoints = _PATHS_DICT[start_and_finish]["curr_waypoints"]
            visited = _PATHS_DICT[start_and_finish]["visited"]
        else:
            raise Exception("Unrecognized destinations")
        dijkstra_waypoint_list.append(curr_waypoints)
        # plot = Plotting(s_goals[stop_sequence[i_stop]], s_goals[stop_sequence[i_stop + 1]])
        # plot.animation(curr_waypoints, visited, "Dijkstra's Algorithm Animation")  # animation generation
    fly(dijkstra_waypoint_list)
user_input_destinations = ["Between the Traffic", "Into the Tree", "Concrete Plaza", "Brick Plaza"]
fly_to_user_input(user_input_destinations)

# print("Flying...")
# current_xy = 0, 0, -50
# for waypoints in _TEST_DIJKSTRA_WAYPOINT_LISTS:
#     i = 0
#     for waypoint in reversed(waypoints):
#         i += 1
#         if i > 1 and i < len(waypoints) - 1:
#             prev = waypoints[i - 2]
#             curr = waypoints[i - 1]
#             next = waypoints[i]
#             if (curr[0] - prev[0] == next[0] - curr[0] and curr[1] - prev[1] == next[1] - curr[1]):
#                 continue
#         new_waypoint = (waypoint[1] - 500), (waypoint[0] + _CORRECTION - 500), -120
#         # current_position = current_xy[0], current_xy[1]
#         yaw = 0 #math.degrees(math.atan2(current_xy[1] - new_waypoint[1], current_xy[0] - new_waypoint[0]))
#         # print("new_waypoint:", new_waypoint)
#         # print("current_xy:", current_xy)
#         # print("vector to new waypoint:", current_xy[1] - new_waypoint[1])
#         # print(f"yaw degree: {yaw}")
#         yaw_mode = airsim.YawMode(is_rate=False, yaw_or_rate=yaw)
#         move_future = client.moveToPositionAsync(new_waypoint[0], new_waypoint[1], new_waypoint[2], 10, drivetrain=airsim.DrivetrainType.ForwardOnly, yaw_mode=yaw_mode)
#         while not move_future._set_flag:
#             move_future._loop.start()
#             distance_sensor_data = client.getDistanceSensorData()
#             # dd = pprint.pformat(distance_sensor_data)
#             # print("distance_sensor_data: %s" % dd)
#             if (distance_sensor_data.distance < 20):
#                 client.cancelLastTask()
#                 client.hoverAsync().join()
#                 exit()

#         move_future.join()
#         # client.hoverAsync().join()
#         # time.sleep(8)

#         current_pose = client.simGetVehiclePose().position
#         current_xy = current_pose.x_val, current_pose.y_val

#     # Descend and hover for dropoff

#     client.hoverAsync().join()
#     client.moveToPositionAsync((waypoints[0][1] - 500), (waypoints[0][0] + _CORRECTION - 500), -5, 10).join()
#     state = client.getMultirotorState()
#     print("state: %s" % pprint.pformat(state))

# airsim.wait_key('Press any key to take images')
# # get camera images from the car
# responses = client.simGetImages([
#     airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
#     airsim.ImageRequest("1", airsim.ImageType.DepthPerspective, True), #depth in perspective projection
#     airsim.ImageRequest("1", airsim.ImageType.Scene), #scene vision image in png format
#     airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGBA array
# print('Retrieved images: %d' % len(responses))

# tmp_dir = os.path.join(tempfile.gettempdir(), "airsim_drone")
# print ("Saving images to %s" % tmp_dir)
# try:
#     os.makedirs(tmp_dir)
# except OSError:
#     if not os.path.isdir(tmp_dir):
#         raise

# for idx, response in enumerate(responses):

#     filename = os.path.join(tmp_dir, str(idx))

#     if response.pixels_as_float:
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
#         airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
#     elif response.compress: #png format
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#         airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
#     else: #uncompressed array
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#         img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) # get numpy array
#         img_rgb = img1d.reshape(response.height, response.width, 3) # reshape array to 4 channel image array H X W X 3
#         cv2.imwrite(os.path.normpath(filename + '.png'), img_rgb) # write to png

airsim.wait_key('Press any key to reset to original state')
endSession()

