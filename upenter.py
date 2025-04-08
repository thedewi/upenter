def main():
    import win32gui, win32process, win32api, win32con, ctypes, time

    processes_to_find = ["mintty", "wsl", "cmd"]

    def eval_hwnd(hwnd, _):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        try:
            hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, pid)
        except:
            return
        if any(
            p in win32process.GetModuleFileNameEx(hproc, None).lower()
            for p in processes_to_find
        ) and win32gui.IsWindowVisible(hwnd):
            hwnds_found.append(hwnd)

    hwnds_found = []
    win32gui.EnumWindows(eval_hwnd, None)

    VK_UP = 0x26
    VK_ENTER = 0x0D
    meta_keys = [
        0xA0,  # VK_LSHIFT
        0xA1,  # VK_RSHIFT
        0xA2,  # VK_LCTRL
        0xA3,  # VK_RCTRL
        0xA4,  # VK_LALT
        0xA5,  # VK_RALT
    ]

    previous_hwnd = win32gui.GetForegroundWindow()
    ctypes.windll.user32.SetForegroundWindow(hwnds_found[0])
    time.sleep(0.1)

    while any(
        (ctypes.windll.user32.GetAsyncKeyState(k) & 0x8000) != 0 for k in meta_keys
    ):
        time.sleep(0.05)

    ctypes.windll.user32.keybd_event(VK_UP, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_UP, 0, 2, 0)
    ctypes.windll.user32.keybd_event(VK_ENTER, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_ENTER, 0, 2, 0)
    ctypes.windll.user32.SetForegroundWindow(previous_hwnd)


if __name__ == "__main__":
    main()
