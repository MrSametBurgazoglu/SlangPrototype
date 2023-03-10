import glfw, skia
from OpenGL import GL

WIDTH, HEIGHT = 640, 480


class Renderer(object):
    def __init__(self, main_widget):
        if not glfw.init():
            raise RuntimeError('glfw.init() failed')
        self.main_widget = main_widget
        self.main_widget.computed_width = WIDTH
        self.main_widget.computed_height = HEIGHT
        self.widget_on_mouse = None
        self.widget_on_focus = None
        glfw.window_hint(glfw.STENCIL_BITS, 8)
        self.window = glfw.create_window(WIDTH, HEIGHT, '', None, None)
        glfw.make_context_current(self.window)

        self.context = skia.GrDirectContext.MakeGL()
        (fb_width, fb_height) = glfw.get_framebuffer_size(self.window)
        backend_render_target = skia.GrBackendRenderTarget(
            fb_width,
            fb_height,
            0,  # sampleCnt
            0,  # stencilBits
            skia.GrGLFramebufferInfo(0, GL.GL_RGBA8))
        self.surface = skia.Surface.MakeFromBackendRenderTarget(
            self.context, backend_render_target, skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())

    def get_widget_on_mouse(self, widget, x_pos, y_pos):
        current_widget = widget
        while len(current_widget.children) > 0:
            for x in current_widget.children:
                if x.is_inside(x_pos, y_pos):
                    current_widget = x
                    break
            else:
                return current_widget
        return current_widget


    def cursor_pos_changed(self, window, x_pos, y_pos):
        last_widget = self.widget_on_mouse
        if self.widget_on_mouse is None:
            self.widget_on_mouse = self.get_widget_on_mouse(self.main_widget, x_pos, y_pos)
        else:
            if len(self.widget_on_mouse.children) == 0:
                if not self.widget_on_mouse.is_inside(x_pos, y_pos):
                    if self.widget_on_mouse.parent.is_inside(x_pos, y_pos):
                        self.widget_on_mouse = self.get_widget_on_mouse(self.widget_on_mouse.parent, x_pos, y_pos)
                    else:
                        self.widget_on_mouse = self.get_widget_on_mouse(self.main_widget, x_pos, y_pos)
            else:
                if self.widget_on_mouse.is_inside(x_pos, y_pos):
                    self.widget_on_mouse = self.get_widget_on_mouse(self.widget_on_mouse, x_pos, y_pos)
                else:
                    self.widget_on_mouse = self.get_widget_on_mouse(self.main_widget, x_pos, y_pos)

    def mouse_button_clicked(self, window, button, action, mods):
        if action != glfw.PRESS:
            return
        current_widget = self.widget_on_mouse  # widget in mouse position
        while "MouseButtonInput" not in current_widget.extend_classes:
            current_widget = current_widget.parent  # find widget has connection to mouse input
            if current_widget is None:
                return
        if "button_clicked" in current_widget.extend_classes["MouseButtonInput"].connections:
            function_to_execute = current_widget.extend_classes["MouseButtonInput"].connections["button_clicked"]
            function_to_execute.execute_function()

    def char_input(self, window, character):
        print("character", character)

    def destroy(self):
        self.context.abandonContext()
        glfw.terminate()

    def start_loop(self):
        GL.glClearColor(1, 1, 1, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        start_position = [0, 0]
        with self.surface as canvas:
            self.main_widget.compute_size()
            self.main_widget.compute_position(start_position)
            self.main_widget.draw(canvas)
        self.surface.flushAndSubmit()
        glfw.set_cursor_pos_callback(self.window, self.cursor_pos_changed)
        glfw.set_char_callback(self.window, self.char_input)
        glfw.set_mouse_button_callback(self.window, self.mouse_button_clicked)
        glfw.swap_buffers(self.window)
        while (glfw.get_key(self.window, glfw.KEY_ESCAPE) != glfw.PRESS
               and not glfw.window_should_close(self.window)):
            glfw.wait_events()
