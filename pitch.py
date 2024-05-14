import subprocess
import os

# Colors!

White = "\033[37m"
Cyan = "\033[36m"
Purple = "\033[35m"
Green = "\033[32m"
Red = "\033[31m"
Yellow = "\033[33m" 
Blue = "\033[34m"
Reset = "\033[0m"

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e}")
        return None

def get_username():
    return run_command(['whoami'])

def get_hostname():
    return run_command(['uname', '-n'])

def get_distro_name():
    if os.path.exists('/bin/lsb_release'):
        result = subprocess.run(['lsb_release', '-d'], capture_output=True, text=True)
        distro_full_info = result.stdout.strip()
        distro_name = distro_full_info.split(':')[1].strip()
        return distro_name
    else:
        return 'Unknown or redhut distro'

def get_window_manager():
    if os.path.exists('/bin/wmctrl'):
        wm = subprocess.run(['wmctrl', '-m'], capture_output=True, text=True)
        wm_name = wm.stdout.split('\n')[0].split(':')[1].strip()
        return wm_name
    else:
        wm_name = "try to install/update wmctrl"
        return wm_name

def get_shell():
    shell_path = os.getenv('SHELL')
    if shell_path:
        return shell_path.split('/')[-1]
    else:
        return "Unknown"

def get_memory_info():
    result = run_command(['free', '-h'])
    if result:
        for line in result.split('\n'):
            if 'Mem:' in line:
                return line.split()[2]
    return "Unknown"

def get_total_memory():
    result = run_command(['free', '-h'])
    if result:
        for line in result.split('\n'):
            if 'Mem:' in line:
                return line.split()[1]
    return "Unknown"

def get_kernel_info():
    return run_command(['uname', '-r'])

def get_openrc_system():
    if os.path.exists('/bin/openrc'):
        return 'openrc'
    elif os.path.exists('/bin/runit'):
        return 'runit'
    elif os.path.exists('/bin/systemctl'):
        return 'systemd'
    elif os.path.exist('/bin/dinit'):
        return 'dinit'
    else:
        return 'Unknown'

if "artix" in get_distro_name().lower():
    def print_logo():
        print(Cyan + "   ___       __  _      ")
        print("  / _ | ____/ /_(_)_ __")
        print(" / __ |/ __/ __/ /\\ \\ /")
        print("/_/ |_/_/  \\__/_//_\\_\\ " + Reset)
        return ""

elif "arch" in get_distro_name().lower():
    def print_logo():
        print(Cyan + "   ___           __ ")
        print("  / _ | ________/ / ")
        print(" / __ |/ __/ __/ _ \\")
        print("/_/ |_/_/  \\__/_//_/" + Reset)
        return ""

elif "void" in get_distro_name().lower():
    def print_logo():
        print(Green + " _   __     _    __")
        print("| | / /__  (_)__/ /")
        print("| |/ / _ \\/ / _  / ")
        print("|___/\\___/_/\\_,_/  " + Reset)
        return ""

elif "gentoo" in get_distro_name().lower():
    def print_logo():
        print(Cyan + "  _____         __          ")
        print(" / ___/__ ___  / /____  ___ ")
        print("/ (_ / -_) _ \\/ __/ _ \\/ _ \\")
        print("\\___/\\__/_//_/\\__/\\___/\\___/" + Reset)
        return ""

else:
    def print_logo():
        print(Green + "   ___  _ __      __ ")
        print("  / _ \\(_) /_____/ / ") 
        print(" / ___/ / __/ __/ _ \\") 
        print("/_/  /_/\\__/\\__/_//_/" + Reset)
        return ""

# Here you can configurate wich information would display 

print()
print(print_logo())
print("╭─────      ───────╮")
#print("User:", White + get_username() + Reset)
#print("Hname:", White + get_hostname() + Reset)
print("Distro:", White + get_distro_name() + Reset)
print("Kernel:", White + get_kernel_info() + Reset)
print("WM: ", White + get_window_manager() + Reset, sep = "")
print("Shell:", White + get_shell() + Reset)
print("Init system:", White + get_openrc_system() + Reset)
print("╰─────      ───────╯")
print()
