from Widgets.MainWidget import MainWidget
from Widgets.Widget import Widget
from Widgets.Box import BoxWidget
from Widgets.ColorRect import ColorRectWidget
from Widgets.ImageRect import ImageRectWidget
from Widgets.TextWidget import TextWidget

from Inputs.MouseButtonInput import MouseButtonInput

elements = {
    "MainWidget": MainWidget,
    "Widget": Widget,
    "Box": BoxWidget,
    "ColorRect": ColorRectWidget,
    "ImageRect": ImageRectWidget,
    "TextWidget": TextWidget,
}

extend_classes = {
    "MouseButtonInput": MouseButtonInput
}

