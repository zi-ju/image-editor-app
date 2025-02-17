from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt


def calculate_initial_scale_factor(image, image_label):
    # Get original image size
    orig_width, orig_height = image.size
    # Get label size
    label_width = image_label.width()
    label_height = image_label.height()

    scale_factor = 1.0

    # Scale if image is larger than label
    if orig_width > label_width or orig_height > label_height:
        # Calculate scale factors for width and height
        width_ratio = label_width / orig_width
        height_ratio = label_height / orig_height
        # Use the smaller ratio to fit the image
        scale_factor = min(width_ratio, height_ratio)

    return scale_factor


def display_image(image, image_label, size_label, scale_label, scale_factor):
    # Get original image size
    orig_width, orig_height = image.size

    # Convert PIL Image to QImage
    image = image.convert("RGB")
    qimg = QImage(image.tobytes(), orig_width, orig_height,
                  orig_width * 3, QImage.Format_RGB888)

    # Convert to QPixmap
    pixmap = QPixmap.fromImage(qimg)

    # Scale the image
    scaled_pixmap = pixmap.scaled(
        int(orig_width * scale_factor),
        int(orig_height * scale_factor),
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )

    # Calculate and display scale percentage
    scale_percentage = scale_factor * 100
    scale_label.setText(f"Scale: {scale_percentage:.1f}%")

    # Display scaled image
    image_label.setPixmap(scaled_pixmap)
    # Display original image size
    size_label.setText(f"Original image size: {orig_width}x{orig_height}")
