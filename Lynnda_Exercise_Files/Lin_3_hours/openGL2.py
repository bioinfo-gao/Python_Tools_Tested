from OpenGL.GL import glClearColor, glClear, GL_COLOR_BUFFER_BIT
import glfw

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "PyOpenGL in Python", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(0.0, 0.0, 0.0, 1.0)   # ← PyOpenGL 调用 OpenGL API
        glClear(GL_COLOR_BUFFER_BIT)        # ← 同上

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()