import sys
import math
import pygame

class Station:
    """
    車站
    """

    def __init__(self, name: str, pos: tuple[float, float], nearby = []):
        """
        車站

        Args:
            name (str): 站名
            pos (tuple): 座標
            nearby (list[str], optional): 鄰近車站名稱
        """
        self._name = name
        self._pos = pos
        self._nearby = nearby

    def __str__(self):
        return "{}({}, {})".format(self._name, self._pos[0], self._pos[1])

    @property
    def name(self) -> str:
        """
        車站名稱

        Returns:
            str: 車站名稱
        """
        return self._name

    @property
    def pos(self) -> tuple[float, float]:
        """
        車站座標

        Returns:
            tuple: 車站座標 格式：(x, y)
        """
        return self._pos

    @property
    def nearby(self) -> list[str]:
        """
        相鄰車站名稱

        Returns:
            list[str]: 相鄰車站名稱
        """
        return self._nearby

class Path:
    """
    路徑
    """

    def __init__(self, stations: list[Station]):
        """
        路徑

        Args:
            stations (list[Station]): 車站列表
        """
        self._stations = stations

    @staticmethod
    def _minDistance(distances: dict) -> tuple[str, float]:
        """
        找出列表中尚未marked的最近車站

        Args:
            distances (dict): 路徑列表

        Returns:
            tuple: (最近車站鍵名, 最近車站距離)
        """
        minIndex = list(distances.keys())[0]
        minVal = math.inf
        for name, data in distances.items():
            if data['distance'] < minVal and data['marked'] == False:
                minIndex = name
                minVal = data['distance']
        return minIndex, minVal

    def findShortestPath(self, start_station: Station, end_station: Station) -> list:
        """
        尋找從A車站到B車站的最短路徑
        基於Dijkstra演算法

        Args:
            start_station (Station): 起點車站
            end_station (Station): 終點車站

        Returns:
            list: 路徑列表
        """
        distances = dict()
        for station in self._stations:
            distances[station.name] = {"distance": math.inf, "single_distance": math.inf, "marked": False, "from": None}
        distances[start_station.name]['marked'] = True
        distances[start_station.name]['distance'] = 0
        distances[start_station.name]['single_distance'] = 0
        station = start_station
        for _ in self._stations:
            for near_station in self.getNearStations(station):
                dis = Path.getStationsDistance(station, near_station)
                full_dis = dis + distances[station.name]['distance']
                # print("begin: {}, end: {}, {}, {}".format(station.name, near_station.name, dis, distances[near_station.name]['distance']))
                if full_dis < distances[near_station.name]['distance'] and distances[near_station.name]['marked'] == False:
                    distances[near_station.name]['single_distance'] = dis
                    distances[near_station.name]['distance'] = full_dis
                    distances[near_station.name]['from'] = station.name
            minIndex, minVal = Path._minDistance(distances)
            distances[minIndex]['marked'] = True
            # print("{} to {}, dis=".format(station.name, minIndex))
            # print(distances)
            station = self.getStationByName(minIndex)
        # print(distances)
        path = []
        last_station = end_station.name
        path.insert(0, {"name": last_station, "distance": distances[last_station]['single_distance']})
        while True:
            path.insert(0, {"name": distances[last_station]['from'], "distance": distances[last_station]['single_distance']})
            last_station = distances[last_station]['from']
            if last_station == start_station.name: break
        return path

    def getStationByName(self, name: str) -> Station:
        """
        透過站名獲取車站

        Args:
            name (str): 站名

        Returns:
            Station: 車站
        """
        return [station for station in self._stations if station.name == name][0]

    def getNearStations(self, station: Station) -> list[Station]:
        """
        獲取鄰近車站

        Args:
            station (Station): 車站

        Returns:
            list[Station]: 鄰近車站
        """
        near_stations = list()
        for near_station_name in station.nearby:
            near_station = self.getStationByName(near_station_name)
            if near_station:
                near_stations.append(near_station)
        return near_stations

    @staticmethod
    def getStationsDistance(start_station: Station, end_station: Station) -> int:
        """
        獲取兩車站間的距離

        Args:
            start_station (Station): 車站1
            end_station (Station): 車站2

        Returns:
            int: 距離
        """
        distance = math.sqrt(
            ( abs(start_station.pos[0] - end_station.pos[0]) ** 2 )
            +
            ( abs(start_station.pos[1] - end_station.pos[1]) ** 2 )
            )
        return distance


class GUI:
    """
    GUI
    """

    def __init__(self):
        """
        GUI
        """

        # 初始化pygame
        pygame.init()

        # 設置主屏窗口
        self._screen = pygame.display.set_mode((800, 800))

        # 設置窗口標題
        pygame.display.set_caption('捷運最短路徑推算')

        # 引入字體類型
        self._f = pygame.font.Font('./fonts/NotoSansTC-Regular.otf', 24)

        # 加載背景圖
        bg_surface = pygame.image.load("./images/background.png").convert()
        # 繪製背景圖
        self._screen.blit(bg_surface, (0, 0))

    def drawStationsPoint(self, stations: list[Station]):
        """
        繪製所有車站的標記點

        Args:
            stations (list[Station]): 車站列表
        """
        for station in stations:
            pygame.draw.circle(self._screen, (255, 0, 0), station.pos, 10)

    def drawStationsWay(self, stations: list[Station]):
        """
        繪製所有車站的可能路徑

        Args:
            stations (list[Station]): 車站列表
        """
        for station in stations:
            for near_station_name in station.nearby:
                near_station = [station for station in stations if station.name == near_station_name][0]
                if near_station:
                    pygame.draw.line(self._screen, (127, 0, 0), station.pos, near_station.pos, width=1)

    def drawStationsPath(self, mrt_path: Path, path: list):
        """
        繪製一條車站到車站間的路徑

        Args:
            mrt_path (Path): Path Object
            path (list): 路徑列表
        """
        for i in range(len(path) - 1):
            pygame.draw.line(self._screen, (0, 0, 255), mrt_path.getStationByName(path[i]['name']).pos, mrt_path.getStationByName(path[i+1]['name']).pos, width=4)

    def drawInfoText(self, text: str, color = (0, 0, 255), bg_color = (255, 255, 255)):
        """
        繪製資訊文字

        Args:
            text (str): 文字內容
            color (tuple, optional): 顏色 Defaults to (0, 0, 255).
            bg_color (tuple, optional): 背景顏色 Defaults to (255, 255, 255).
        """
        # 生成文本信息，第一個參數文本內容；第二個參數，字體是否平滑；
        # 第三個參數，RGB模式的字體顏色；第四個參數，RGB模式字體背景顏色；
        t = self._f.render(text, True, color, bg_color)
        #獲得顯示對象的rect區域坐標
        textRect = t.get_rect()
        # 設置顯示對象居中
        textRect.topleft = (20, 20)
        # 將準備好的文本信息，繪制到主屏幕 Screen 上。
        self._screen.blit(t, textRect)

    def waitClose(self):
        """
        等待視窗關閉
        """
        # 固定代碼段，實現點擊"X"號退出界面的功能，幾乎所有的pygame都會使用該段代碼
        while True:
            # 循環獲取事件，監聽事件狀態
            for event in pygame.event.get():
                # 判斷用戶是否點了"X"關閉按鈕,並執行if代碼段
                if event.type == pygame.QUIT:
                    #卸載所有模塊
                    pygame.quit()
                    #終止程序，確保退出程序
                    sys.exit()
            pygame.display.flip() #更新屏幕內容