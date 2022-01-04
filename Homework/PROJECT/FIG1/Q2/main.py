import math
import random
import MRT

# 定義車站資訊
stations_info = {
    "南港展覽館": {
        "pos": (732, 440),
        "nearby": [
            "內湖", "動物園"
        ]
    },
    "內湖": {
        "pos": (679, 266),
        "nearby": [
            "南港展覽館", "動物園", "台北車站", "大橋頭"
        ]
    },
    "動物園": {
        "pos": (604, 730),
        "nearby": [
            "南港展覽館", "內湖", "六張犁"
        ]
    },
    "六張犁": {
        "pos": (449, 575),
        "nearby": [
            "新店", "永安市場", "台北車站"
        ]
    },
    "台北車站": {
        "pos": (266, 440),
        "nearby": [
            "內湖", "大橋頭", "亞東醫院", "永安市場", "六張犁"
        ]
    },
    "大橋頭": {
        "pos": (235, 325),
        "nearby": [
            "內湖", "蘆洲", "永安市場", "台北車站"
        ]
    },
    "永安市場": {
        "pos": (270, 624),
        "nearby": [
            "六張犁", "台北車站", "大橋頭", "蘆洲", "亞東醫院", "新店"
        ]
    },
    "蘆洲": {
        "pos": (87, 189),
        "nearby": [
            "大橋頭", "永安市場"
        ]
    },
    "亞東醫院": {
        "pos": (114, 614),
        "nearby": [
            "台北車站", "永安市場"
        ]
    },
    "新店": {
        "pos": (376, 766),
        "nearby": [
            "六張犁", "永安市場"
        ]
    }
}

def getRandomStations(stations: list[MRT.Station], number = 3) -> list[MRT.Station]:
    """
    隨機獲取多個目標車站(不重複)

    Args:
        stations (list[MRT.Station]): 車站列表
        number (int, optional): 數量 Defaults to 3.

    Returns:
        list[MRT.Station]: 隨機選出的車站
    """
    shuffle_stations = stations.copy()
    random.shuffle(shuffle_stations)
    return shuffle_stations[0:number]

if __name__ == "__main__":

    # 創建車站物件
    stations = [MRT.Station(name, info['pos'], info['nearby']) for name, info in stations_info.items()]

    # 宣告MRT相關物件
    gui = MRT.GUI()
    path = MRT.Path(stations)

    # 設置起點站
    start_station = stations[0]

    # 刪除起點站，以避免被抽中作為目標站
    stations_without_start = stations.copy()
    del stations_without_start[stations_without_start.index(start_station)]
    # 隨機抽出目標站
    target_stations = getRandomStations(stations_without_start)

    # 印出起點站和目標站相關資訊
    print("起始站：{}".format(start_station.name))
    print("目標站：")
    for station in target_stations:
        print("\t{}".format(station.name))

    # 繪製所有車站的可能路徑
    gui.drawStationsWay(stations)

    # 計算所有目標車站的最佳路徑並繪製
    print("\n最佳路徑：")
    begin_station = start_station
    target_stations_copy = target_stations.copy()
    for i in range(len(target_stations_copy)):
        # 從剩餘目標車站中挑出最近的一個先走
        min_dis = math.inf
        min_station = begin_station
        min_shortest_path = None
        for station in target_stations_copy:
            dis = 0
            # print("begin: {}, target: {}".format(begin_station.name, station.name))
            shortest_path = path.findShortestPath(begin_station, station)
            for p in shortest_path:
                dis += p['distance']
            if dis < min_dis:
                min_dis = dis
                min_station = station
                min_shortest_path = shortest_path
        # 從列表中刪除已到達的車站
        del target_stations_copy[target_stations_copy.index(min_station)]
        print("\t{}. {} => {}".format(i + 1, begin_station, min_station))
        for j in range(len(min_shortest_path) - 1):
            print("\t   →Step{}: {} -> {}".format(j + 1, min_shortest_path[j]['name'], min_shortest_path[j + 1]['name']))
        # 繪製從起點到終點的路徑
        gui.drawStationsPath(path, min_shortest_path)
        begin_station = min_station

    # 繪製所有車站的標記點
    gui.drawStationsPoint(stations)

    # 在圖上印出路徑相關資訊
    target_stations_text = ""
    i = 0
    for station in target_stations:
        target_stations_text += station.name + (", " if i != len(target_stations) - 1 else "")
        i += 1
    gui.drawInfoText("起點站：{} 目標站：{}".format(start_station.name, target_stations_text))

    # 等待視窗關閉
    gui.waitClose()