import subprocess
import os

Cyan = "\033[36m"
Purple = "\033[35m"
Green = "\033[32m"
Red = "\033[31m"
Yellow = "\033[33m" 
Blue = "\033[34m"
Reset = "\033[0m"

def get_username():
    result = subprocess.run(['whoami'], capture_output=True, text=True)
    username = result.stdout.strip()
    return username

def get_hostname():
    result = subprocess.run(['uname', '-n'], capture_output=True, text=True)
    hostname = result.stdout.strip()
    return hostname

def get_distro_name():
    result = subprocess.run(['lsb_release', '-d'], capture_output=True, text=True)
    distro_full_info = result.stdout.strip()
    distro_name = distro_full_info.split(':')[1].strip()
    return distro_name

def get_window_manager():
    wm = subprocess.run(['wmctrl', '-m'], capture_output=True, text=True)
    wm_name = wm.stdout.split('\n')[0].split(':')[1].strip()
    wlctrl_path = '/bin/wmctrl'
    display_env = os.getenv('DISPLAY')
    if display_env:
        if wm_name:
            return wm_name
        elif os.path.exist(wlctrl_path):
            return 'Unknown'
        else:
            return 'Try to install wmctrl'
    else:
        return 'Unknown'

def get_shell():
    shell_path = os.getenv('SHELL')
    if shell_path:
        return shell_path.split('/')[-1]
    else:
        return "Unknown"

def get_memory_info():
    result = subprocess.run(['free', '-h'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    lines = output.split('\n')
    for line in lines:
        if 'Mem:' in line:
            words = line.split()
            memory_used = words[2]
            return memory_used

def get_total_memory():
    result = subprocess.run(['free', '-h'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    lines = output.split('\n')
    for line in lines:
        if 'Mem:' in line:
            words = line.split()
            total_memory = words[1]
            return total_memory

def get_kernel_info():
    result = subprocess.run(['uname', '-r'], capture_output=True, text=True)
    kernel = result.stdout.strip()
    return kernel

def get_init_system():
    systemd_path = '/run/systemd/system'
    runit_path = '/etc/runit'
    openrc_path = '/usr/bin/openrc-init'
    if subprocess.run(['systemctl'], capture_output=True, text=True).returncode == 0:
        return 'systemd'
    elif os.path.exists(runit_path):
        return 'runit'
    elif os.path.exists(openrc):
        return 'openrc'   
    else:
        return 'unknown'



if "void" in get_distro_name().lower():
    def print_logo():
        print(Green + " _    __      _     __")
        print("| |  / /___  (_)___/ /")
        print("| | / / __ \\/ / __  /")
        print("| |/ / /_/ / / /_/ / ")
        print("|___/\\____/_/\\__,_/" + Reset)
        return ""
elif "arch" in get_distro_name().lower():
    def print_logo():
        print(Cyan + "    ___              __ ")
        print("   /   |  __________/ /_")
        print("  / /| | / ___/ ___/ __ \\")
        print(" / ___ |/ /  / /__/ / / /")  
        print("/_/  |_/_/   \\___/_/ /_/ " + Reset)
        return ""
elif "gentoo" in get_distro_name().lower():
    def print_logo():
        print(Cyan + "   ______           __            ")
        print("  / ____/__  ____  / /_____  ____ ")
        print(" / / __/ _ \\/ __ \\/ __/ __ \\/ __ \\")
        print("/ /_/ /  __/ / / / /_/ /_/ / /_/ /")
        print("\\____/\\___/_/ /_/\\__/\\____/\\____/ " + Reset)
        return ""
elif "artix" in get_distro_name().lower():
    def print_logo():
        print(Cyan + "    ___         __  _     ")
        print("   /   |  _____/ /_(_)  __")
        print("  / /| | / ___/ __/ / |/_/")
        print(" / ___ |/ /  / /_/ />  <  ")
        print("/_/  |_/_/   \\__/_/_/|_|  " + Reset)
        return ""
else:
    def print_logo():
        print(Green + "    ____  _ __       __ ")
        print("   / __ \\(_) /______/ /_ ")
        print("  / /_/ / / __/ ___/ __ \\")
        print(" / ____/ / /_/ /__/ / / /")
        print("/_/   /_/\\__/\\___/_/ /_/ " + Reset)
        return ""



print(print_logo())
print("╭────────────────╮")
print("│", Red + "" + Reset, "user:        │", Red + get_username() + Reset)
print("│", Yellow + "" + Reset, "hname:       │", Yellow + get_hostname() + Reset)
print("│", Green + "" + Reset, "distro:      │", Green + get_distro_name() + Reset)
print("│", Purple + "󰌽" + Reset, "kernel:      │", Purple + get_kernel_info() + Reset)
print("│ ", Cyan + "" + Reset, " WM:          │ ", Cyan + get_window_manager() + Reset, sep = "")
print("│", Yellow + "" + Reset, "shell        │", Yellow + get_shell() + Reset)
print("│", Purple + "󰜎" + Reset, "init system: │", Purple + get_init_system() + Reset)
print("│", Cyan + "" + Reset, "memory:      │", Cyan + get_memory_info(), "|", get_total_memory() + Reset)
print("├────────────────┤")
print("│  colors:      │", Red + "  " + Yellow + "  " + Green + "  " + Purple + "  " + Cyan + "  " + Reset, " ")
print("╰────────────────╯")
