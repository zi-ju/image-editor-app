from PySide6.QtWidgets import QFileDialog, QLabel, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PIL import Image


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor")
        self.setGeometry(100, 100, 800, 600)

        # Initialize image path and loaded image object
        self.image_path = None
        self.image = None

        # QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 50, 700, 500)

        # Button to load an image
        self.load_button = QPushButton("Load Image", self)
        self.load_button.setGeometry(50, 550, 100, 30)
        self.load_button.clicked.connect(self.load_image)

        # Button to crop the image
        self.crop_button = QPushButton("Crop Image", self)
        self.crop_button.setGeometry(200, 550, 100, 30)
        self.crop_button.clicked.connect(self.crop_image)

    def load_image(self):
        # Load image from file
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def display_image(self, image):
        # Convert PIL Image to QImage
        image = image.convert("RGB")
        width, height = image.size

        # Convert to QImage
        qimg = QImage(image.tobytes(), width, height, width * 3, QImage.Format_RGB888)

        # Create QPixmap
        pixmap = QPixmap.fromImage(qimg)

        # Get label size
        label_width = self.image_label.width()
        label_height = self.image_label.height()

        # Scale image only if it's larger than the label, maintaining aspect ratio
        if width > label_width or height > label_height:
            scaled_pixmap = pixmap.scaled(label_width, label_height,
                                          Qt.KeepAspectRatio,
                                          Qt.SmoothTransformation)
        else:
            # If image is smaller than label, use original size
            scaled_pixmap = pixmap

        # Set the pixmap to the label
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

    def crop_image(self):
        pass

