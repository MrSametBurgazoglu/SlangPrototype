import contextlib, glfw, skia
from OpenGL import GL
from Renderer import utils

WIDTH, HEIGHT = 640, 480


class Renderer(object):
    def __init__(self, main_widget):
        if not glfw.init():
            raise RuntimeError('glfw.init() failed')
        self.main_widget = main_widget
        self.main_widget.computed_width = WIDTH
        self.main_widget.computed_height = HEIGHT
        self.widget_on_mouse = None
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

    def get_widget_on_mouse(self, x_pos, y_pos):
        current_widget = self.main_widget
        while True:
            if len(current_widget.children) == 0:
                break
            for x in current_widget.children:
                # print(x_pos, y_pos, x.computed_pos_x, x.computed_pos_y, x.computed_width, x.computed_height)
                # print(x.computed_pos_x < x_pos < x.computed_pos_x + x.computed_width)
                # print(x.computed_pos_y < y_pos < x.computed_pos_y + x.computed_height)
                if utils.in_rect(x_pos, y_pos, x.computed_pos_x, x.computed_pos_y, x.computed_width, x.computed_height):
                    current_widget = x
                    break
            else:
                break
    def cursor_pos_changed(self, window, x_pos, y_pos):
        self.get_widget_on_mouse(x_pos, y_pos)

    def destroy(self):
        self.context.abandonContext()
        glfw.terminate()

    def init_draw_loop(self):
        GL.glClearColor(1, 1, 1, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        with self.surface as canvas:
            self.main_widget.compute_size()
            self.main_widget.compute_position()
            self.main_widget.draw(canvas)
        self.surface.flushAndSubmit()
        glfw.set_cursor_pos_callback(self.window, self.cursor_pos_changed)
        glfw.swap_buffers(self.window)
        while (glfw.get_key(self.window, glfw.KEY_ESCAPE) != glfw.PRESS
               and not glfw.window_should_close(self.window)):
            glfw.wait_events()
