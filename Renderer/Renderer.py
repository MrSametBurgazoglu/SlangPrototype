import contextlib, glfw, skia
from OpenGL import GL

WIDTH, HEIGHT = 640, 480


class Renderer(object):
    def __init__(self, main_widget):
        if not glfw.init():
            raise RuntimeError('glfw.init() failed')
        self.main_widget = main_widget
        self.main_widget.computed_width = WIDTH
        self.main_widget.computed_height = HEIGHT
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

    def destroy(self):
        self.context.abandonContext()
        glfw.terminate()

    def init_draw_loop(self):
        GL.glClearColor(1, 1, 1, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        with self.surface as canvas:
            self.main_widget.render(canvas)
            self.main_widget.draw(canvas)
        self.surface.flushAndSubmit()
        glfw.swap_buffers(self.window)
        while (glfw.get_key(self.window, glfw.KEY_ESCAPE) != glfw.PRESS
               and not glfw.window_should_close(self.window)):
            glfw.wait_events()
