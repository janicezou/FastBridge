import text
nan=""
section_words = {'start': -1, '0': 49, '1.1': 111, '1.10': 181, '1.11': 284, '1.12': 362, '1.13': 397, '1.14': 414, '1.15': 487, '1.16': 550, '1.17': 591, '1.18': 654, '1.19': 705, '1.2': 795, '1.20': 932, '1.3': 986, '1.4': 1027, '1.5': 1060, '1.6': 1116, '1.7': 1187, '1.8': 1317, '1.9': 1432, '10.1': 1547, '10.10': 1654, '10.11': 1717, '10.12': 1781, '10.13': 1826, '10.14': 1898, '10.15': 2000, '10.16': 2149, '10.17': 2303, '10.18': 2405, '10.2': 2547, '10.24': 2548, '10.26': 2549, '10.3': 2652, '10.4': 2748, '10.5': 2803, '10.6': 2882, '10.7': 2971, '10.8': 3035, '10.9': 3144, '2.1': 3196, '2.10': 3220, '2.11': 3359, '2.12': 3466, '2.13': 3567, '2.14': 3700, '2.15': 3724, '2.16': 3757, '2.17': 3781, '2.18': 3842, '2.19': 3897, '2.2': 3941, '2.20': 4014, '2.21': 4146, '2.22': 4240, '2.23': 4281, '2.24': 4345, '2.25': 4453, '2.26': 4491, '2.27': 4623, '2.28': 4656, '2.3': 4693, '2.4': 4707, '2.5': 4780, '2.6': 4895, '2.7': 4947, '2.8': 5034, '2.9': 5151, '3.1': 5210, '3.10': 5323, '3.11': 5414, '3.12': 5496, '3.13': 5567, '3.14': 5709, '3.15': 5806, '3.16': 5885, '3.17': 5910, '3.18': 5997, '3.19': 6013, '3.2': 6058, '3.20': 6149, '3.21': 6209, '3.22': 6313, '3.23': 6385, '3.27': 6386, '3.3': 6416, '3.4': 6442, '3.5': 6482, '3.6': 6540, '3.7': 6624, '3.8': 6682, '3.9': 6750, '4.1': 6762, '4.10': 6847, '4.11': 6872, '4.12': 6932, '4.13': 6974, '4.14': 7030, '4.15': 7050, '4.16': 7130, '4.17': 7239, '4.18': 7258, '4.19': 7284, '4.2': 7361, '4.20': 7473, '4.21': 7500, '4.22': 7552, '4.23': 7585, '4.24': 7598, '4.25': 7626, '4.26': 7687, '4.27': 7834, '4.3': 7887, '4.4': 8034, '4.5': 8080, '4.6': 8232, '4.7': 8360, '4.8': 8460, '4.9': 8475, '5.1': 8584, '5.16': 8585, '5.2': 8649, '5.22': 8650, '5.25': 8651, '5.3': 8791, '5.4': 8891, '5.5': 8988, '5.6': 9096, '5.7': 9256, '5.8': 9362, '5.9': 9430, '6.0': 9431, '6.1': 9548, '6.10': 9618, '6.11': 9675, '6.12': 9783, '6.13': 9846, '6.14': 9962, '6.15': 10013, '6.16': 10066, '6.17': 10184, '6.18': 10249, '6.19': 10345, '6.2': 10391, '6.20': 10497, '6.21': 10576, '6.22': 10643, '6.23': 10731, '6.24': 10798, '6.25': 10885, '6.3': 10937, '6.4': 10957, '6.5': 10994, '6.6': 11104, '6.7': 11184, '6.8': 11302, '6.9': 11391, '7.1': 11475, '7.10': 11581, '7.11': 11647, '7.12': 11704, '7.13': 11815, '7.14': 11941, '7.15': 12023, '7.16': 12104, '7.17': 12193, '7.18': 12332, '7.19': 12465, '7.2': 12537, '7.20': 12619, '7.21': 12733, '7.22': 12796, '7.23': 12967, '7.3': 13082, '7.4': 13120, '7.5': 13167, '7.6': 13218, '7.7': 13297, '7.8': 13395, '7.9': 13512, '8.1': 13588, '8.10': 13710, '8.11': 13781, '8.12': 13879, '8.13': 13996, '8.14': 14044, '8.15': 14116, '8.16': 14143, '8.17': 14178, '8.18': 14307, '8.19': 14385, '8.2': 14470, '8.20': 14525, '8.21': 14555, '8.22': 14601, '8.23': 14660, '8.3': 14740, '8.4': 14845, '8.5': 14958, '8.6': 15053, '8.7': 15119, '8.8': 15253, '8.9': 15301, '9.1': 15355, '9.10': 15399, '9.11': 15484, '9.12': 15509, '9.13': 15629, '9.14': 15681, '9.15': 15798, '9.16': 15836, '9.17': 15928, '9.18': 16041, '9.19': 16123, '9.2': 16227, '9.20': 16318, '9.21': 16389, '9.22': 16504, '9.23': 16594, '9.24': 16646, '9.25': 16741, '9.26': 16800, '9.27': 16895, '9.28': 16945, '9.3': 16990, '9.4': 17030, '9.5': 17072, '9.6': 17081, '9.7': 17139, '9.8': 17235, '9.9': 17320, 'I.7': 17321, 'Tit..': 17322, 'end': -2}
section_list ={'1.1.1': 'start', '0': 'start', '1.1': '0', '1.10': '1.1', '1.11': '1.10', '1.12': '1.11', '1.13': '1.12', '1.14': '1.13', '1.15': '1.14', '1.16': '1.15', '1.17': '1.16', '1.18': '1.17', '1.19': '1.18', '1.2': '1.19', '1.20': '1.2', '1.3': '1.20', '1.4': '1.3', '1.5': '1.4', '1.6': '1.5', '1.7': '1.6', '1.8': '1.7', '1.9': '1.8', '10.1': '1.9', '10.10': '10.1', '10.11': '10.10', '10.12': '10.11', '10.13': '10.12', '10.14': '10.13', '10.15': '10.14', '10.16': '10.15', '10.17': '10.16', '10.18': '10.17', '10.2': '10.18', '10.24': '10.2', '10.26': '10.24', '10.3': '10.26', '10.4': '10.3', '10.5': '10.4', '10.6': '10.5', '10.7': '10.6', '10.8': '10.7', '10.9': '10.8', '2.1': '10.9', '2.10': '2.1', '2.11': '2.10', '2.12': '2.11', '2.13': '2.12', '2.14': '2.13', '2.15': '2.14', '2.16': '2.15', '2.17': '2.16', '2.18': '2.17', '2.19': '2.18', '2.2': '2.19', '2.20': '2.2', '2.21': '2.20', '2.22': '2.21', '2.23': '2.22', '2.24': '2.23', '2.25': '2.24', '2.26': '2.25', '2.27': '2.26', '2.28': '2.27', '2.3': '2.28', '2.4': '2.3', '2.5': '2.4', '2.6': '2.5', '2.7': '2.6', '2.8': '2.7', '2.9': '2.8', '3.1': '2.9', '3.10': '3.1', '3.11': '3.10', '3.12': '3.11', '3.13': '3.12', '3.14': '3.13', '3.15': '3.14', '3.16': '3.15', '3.17': '3.16', '3.18': '3.17', '3.19': '3.18', '3.2': '3.19', '3.20': '3.2', '3.21': '3.20', '3.22': '3.21', '3.23': '3.22', '3.27': '3.23', '3.3': '3.27', '3.4': '3.3', '3.5': '3.4', '3.6': '3.5', '3.7': '3.6', '3.8': '3.7', '3.9': '3.8', '4.1': '3.9', '4.10': '4.1', '4.11': '4.10', '4.12': '4.11', '4.13': '4.12', '4.14': '4.13', '4.15': '4.14', '4.16': '4.15', '4.17': '4.16', '4.18': '4.17', '4.19': '4.18', '4.2': '4.19', '4.20': '4.2', '4.21': '4.20', '4.22': '4.21', '4.23': '4.22', '4.24': '4.23', '4.25': '4.24', '4.26': '4.25', '4.27': '4.26', '4.3': '4.27', '4.4': '4.3', '4.5': '4.4', '4.6': '4.5', '4.7': '4.6', '4.8': '4.7', '4.9': '4.8', '5.1': '4.9', '5.16': '5.1', '5.2': '5.16', '5.22': '5.2', '5.25': '5.22', '5.3': '5.25', '5.4': '5.3', '5.5': '5.4', '5.6': '5.5', '5.7': '5.6', '5.8': '5.7', '5.9': '5.8', '6.0': '5.9', '6.1': '6.0', '6.10': '6.1', '6.11': '6.10', '6.12': '6.11', '6.13': '6.12', '6.14': '6.13', '6.15': '6.14', '6.16': '6.15', '6.17': '6.16', '6.18': '6.17', '6.19': '6.18', '6.2': '6.19', '6.20': '6.2', '6.21': '6.20', '6.22': '6.21', '6.23': '6.22', '6.24': '6.23', '6.25': '6.24', '6.3': '6.25', '6.4': '6.3', '6.5': '6.4', '6.6': '6.5', '6.7': '6.6', '6.8': '6.7', '6.9': '6.8', '7.1': '6.9', '7.10': '7.1', '7.11': '7.10', '7.12': '7.11', '7.13': '7.12', '7.14': '7.13', '7.15': '7.14', '7.16': '7.15', '7.17': '7.16', '7.18': '7.17', '7.19': '7.18', '7.2': '7.19', '7.20': '7.2', '7.21': '7.20', '7.22': '7.21', '7.23': '7.22', '7.3': '7.23', '7.4': '7.3', '7.5': '7.4', '7.6': '7.5', '7.7': '7.6', '7.8': '7.7', '7.9': '7.8', '8.1': '7.9', '8.10': '8.1', '8.11': '8.10', '8.12': '8.11', '8.13': '8.12', '8.14': '8.13', '8.15': '8.14', '8.16': '8.15', '8.17': '8.16', '8.18': '8.17', '8.19': '8.18', '8.2': '8.19', '8.20': '8.2', '8.21': '8.20', '8.22': '8.21', '8.23': '8.22', '8.3': '8.23', '8.4': '8.3', '8.5': '8.4', '8.6': '8.5', '8.7': '8.6', '8.8': '8.7', '8.9': '8.8', '9.1': '8.9', '9.10': '9.1', '9.11': '9.10', '9.12': '9.11', '9.13': '9.12', '9.14': '9.13', '9.15': '9.14', '9.16': '9.15', '9.17': '9.16', '9.18': '9.17', '9.19': '9.18', '9.2': '9.19', '9.20': '9.2', '9.21': '9.20', '9.22': '9.21', '9.23': '9.22', '9.24': '9.23', '9.25': '9.24', '9.26': '9.25', '9.27': '9.26', '9.28': '9.27', '9.3': '9.28', '9.4': '9.3', '9.5': '9.4', '9.6': '9.5', '9.7': '9.6', '9.8': '9.7', '9.9': '9.8', 'I.7': '9.9', 'Tit..': 'I.7', 'end': 'Tit..', 'start': 'start'}
title = "Eutropius, Breviarium (all)"
section_level =  3
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, True, False)