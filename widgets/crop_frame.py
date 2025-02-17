from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt, QRect


class CropFrame(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.crop_rect = None
        self.dragging = False
        self.drag_start = None
        self.setMouseTracking(True)

    def setCropSize(self, width, height):
        if self.pixmap():
            # Calculate the position of top-left corner to center the crop rectangle
            x = (self.pixmap().width() - width) // 2
            y = (self.pixmap().height() - height) // 2
            self.crop_rect = QRect(x, y, width, height)
            self.update()

    def mousePressEvent(self, event):
        if self.crop_rect and self.crop_rect.contains(event.pos()):
            self.dragging = True
            self.drag_start = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging and self.crop_rect:
            delta = event.pos() - self.drag_start
            self.crop_rect.translate(delta)
            if self.crop_rect.left() < 0:
                self.crop_rect.moveLeft(0)
            if self.crop_rect.top() < 0:
                self.crop_rect.moveTop(0)
            if self.crop_rect.right() > self.width():
                self.crop_rect.moveRight(self.width())
            if self.crop_rect.bottom() > self.height():
                self.crop_rect.moveBottom(self.height())
            self.drag_start = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.dragging = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.crop_rect:
            painter = QPainter(self)
            pen = QPen(Qt.red, 2)
            painter.setPen(pen)
            painter.drawRect(self.crop_rect)
