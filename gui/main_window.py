from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QFileDialog,
                               QWidget, QVBoxLayout, QHBoxLayout, QSlider)
from PySide6.QtCore import Qt
from PIL import Image
from widgets.display_image import display_image, calculate_initial_scale_factor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Initialize image
        self.image_path = None
        self.image = None

        # Create image label
        self.image_label = QLabel()
        self.image_label.setFixedSize(1000, 500)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        # Initialize scale factor and scale label
        self.scale_factor = 1.0
        self.scale_label = QLabel()
        layout.addWidget(self.scale_label)

        # Slider to control the scale factor
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setRange(1, 200)  # scale from 1% to 200%
        self.scale_slider.setValue(100)  # default value is 100%
        self.scale_slider.valueChanged.connect(self.update_scale)
        layout.addWidget(self.scale_slider)

        # Image size label
        self.size_label = QLabel()
        layout.addWidget(self.size_label)

        # Create button layout
        button_layout = QHBoxLayout()

        # Load image button
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)
        button_layout.addWidget(self.load_button)

        layout.addLayout(button_layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image File",
            "",
            "Images (*.png *.xpm *.jpg *.jpeg)"
        )
        if file_path:
            self.image = Image.open(file_path)
            self.scale_factor = calculate_initial_scale_factor(self.image, self.image_label)
            display_image(self.image, self.image_label,
                          self.size_label, self.scale_label,
                          self.scale_factor)

    # Update the scale factor based on slider value
    def update_scale(self):
        self.scale_factor = self.scale_slider.value() / 100.0
        if self.image:
            display_image(self.image, self.image_label,
                          self.size_label, self.scale_label,
                          self.scale_factor)
