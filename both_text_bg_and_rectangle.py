
import cv2

# Draw green rectangle
def draw_rectangle(image, top_left, bottom_right, color, thickness):
    """
    Draws a rectangle on the image.
    # Renders a rectangle onto the provided image.
    # @param image: The image where the rectangle will be drawn.
    # @param top_left: Coordinates (x, y) of the rectangle's top-left corner.
    # @param bottom_right: Coordinates (x, y) of the rectangle's bottom-right corner.
    # @param color: The rectangle's color specified in (Blue, Green, Red) format.
    # @param thickness: The width of the rectangle's border.

    """
    cv2.rectangle(image, top_left, bottom_right, color, thickness)

# Add text with shown bg
def add_text_with_background(image, text, position, font, font_scale, font_thickness, text_color, bg_color, opacity, padding=10):
    """
    Adds semi-transparent background and text to an image.
        # Overlays text with a semi-transparent background onto an image.
    # @param image: The target image to modify.
    # @param text: The string to display on the image.
    # @param position: Coordinates (x, y) specifying the location of the text.
    # @param font: The typeface style for the text.
    # @param font_scale: The scaling factor for the text size.
    # @param font_thickness: The thickness of the text characters.
    # @param text_color: The text color in (Blue, Green, Red) format.
    # @param bg_color: The color of the background behind the text (B, G, R).
    # @param opacity: The transparency level of the background (0.0 = fully transparent, 1.0 = fully opaque).
    # @param padding: Extra space around the text for the background.

    """
    overlay = image.copy()
    text_size, baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_width, text_height = text_size
    # Coordinates for the rectangle
    rect_x1 = position[0] - padding
    rect_y1 = position[1] - text_height - padding
    rect_x2 = position[0] + text_width + padding
    rect_y2 = position[1] + baseline + padding
    # Draw the semi-transparent rectangle
    cv2.rectangle(overlay, (rect_x1, rect_y1), (rect_x2, rect_y2), bg_color, -1)
    cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)
    # Add text on top
    cv2.putText(image, text, position, font, font_scale, text_color, font_thickness)


# Load image
image = cv2.imread('assignment-001-given.jpg')
# Parameters
text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 5
text_color = (0, 255, 0)  # Green
bg_color = (0, 0, 0)  # Black
opacity = 0.5
padding = 120
# Text position
img_height, img_width, _ = image.shape
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
text_width, text_height = text_size
text_x = img_width - text_width - padding
text_y = text_height + padding
# Add text with background
add_text_with_background(image, text, (text_x, text_y), font, font_scale, font_thickness, text_color, bg_color, opacity)
# Draw rectangle
draw_rectangle(image, (265, 200), (988, 925), (0, 255, 0), 10)
# Display and save image
cv2.imshow('Done_by_Debrice', image)
cv2.waitKey(0)
cv2.imwrite('assignment_result_Debrice.jpg', image)
cv2.destroyAllWindows()