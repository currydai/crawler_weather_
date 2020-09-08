from PyQt5 import QtCore, QtGui, QtWidgets
from weatherGUI import Ui_weatherGUI
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pandas as pd
import numpy as np
from xpinyin import Pinyin

class MyMainForm(QMainWindow,Ui_weatherGUI):
    def __init__(self,parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton1.clicked.connect(self.display)
    def display(self):
        p = Pinyin()
        province = self.line1.text()

        shenfen=p.get_pinyin(u"%s"%province, '')
        print(shenfen)
        city = self.line2.text()
        District = self.line3.text()
        url = r'http://www.weather.com.cn/textFC/%s.shtml' % shenfen

        data = pd.read_html(url)

        temp = []
        date = []
        for i in data:
            if (len(i.index) == 2):
                temp.append(i.iloc[0, 0:8])
                date.append(i.iloc[0, 2])
                temp.append(i.iloc[1, 0:8])
            else:
                if (i.loc[0, 0] == "%s" % city):
                    for j in range(len(i.index)):
                        temp.append(i.iloc[j, 0:8])
        temp2 = pd.DataFrame(temp)

        temp3 = []
        for i in range(len(temp2.index)):
            if (temp2.iloc[i, 1] == "%s" % District):
                temp3.append(temp2.iloc[i, 2:8])
        temp4 = pd.DataFrame(temp3)
        temp4.index = date
        temp4.columns = temp2.iloc[1, 2:8].tolist()
        print(temp4)
        self.textBrowser11.setText('%s'%date[0])
        self.textBrowser21.setText('%s' % date[1])
        self.textBrowser31.setText('%s' % date[2])
        self.textBrowser41.setText('%s' % date[3])
        self.textBrowser51.setText('%s' % date[4])
        self.textBrowser61.setText('%s' % date[5])
        self.textBrowser71.setText('%s' % date[6])

        self.textBrowser12.setText('%s-%s'%(temp4.iloc[0][0],temp4.iloc[0][3]))
        self.textBrowser22.setText('%s-%s'%(temp4.iloc[1][0],temp4.iloc[1][3]))
        self.textBrowser32.setText('%s-%s'%(temp4.iloc[2][0],temp4.iloc[2][3]))
        self.textBrowser42.setText('%s-%s'%(temp4.iloc[3][0],temp4.iloc[3][3]))
        self.textBrowser52.setText('%s-%s'%(temp4.iloc[4][0],temp4.iloc[4][3]))
        self.textBrowser62.setText('%s-%s'%(temp4.iloc[5][0],temp4.iloc[5][3]))
        self.textBrowser72.setText('%s-%s'%(temp4.iloc[6][0],temp4.iloc[6][3]))

        self.textBrowser13.setText('%s' % (temp4.iloc[0][1]))
        self.textBrowser23.setText('%s' % (temp4.iloc[1][1]))
        self.textBrowser33.setText('%s' % (temp4.iloc[2][1]))
        self.textBrowser43.setText('%s' % (temp4.iloc[3][1]))
        self.textBrowser53.setText('%s' % (temp4.iloc[4][1]))
        self.textBrowser63.setText('%s' % (temp4.iloc[5][1]))
        self.textBrowser73.setText('%s' % (temp4.iloc[6][1]))

        self.textBrowser14.setText('%s-%s'%(temp4.iloc[0][2],temp4.iloc[0][5]))
        self.textBrowser24.setText('%s-%s'%(temp4.iloc[1][2],temp4.iloc[1][5]))
        self.textBrowser34.setText('%s-%s'%(temp4.iloc[2][2],temp4.iloc[2][5]))
        self.textBrowser44.setText('%s-%s'%(temp4.iloc[3][2],temp4.iloc[3][5]))
        self.textBrowser54.setText('%s-%s'%(temp4.iloc[4][2],temp4.iloc[4][5]))
        self.textBrowser64.setText('%s-%s'%(temp4.iloc[5][2],temp4.iloc[5][5]))
        self.textBrowser74.setText('%s-%s'%(temp4.iloc[6][2],temp4.iloc[6][5]))




if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())



