from PyQt5.QtCore import QObject, pyqtSignal

class Foo(QObject):

    closed = pyqtSignal()

    range_changed = pyqtSignal(int, int, name='rangeChanged')

    valueChanged = pyqtSignal([int], ['QString'])
