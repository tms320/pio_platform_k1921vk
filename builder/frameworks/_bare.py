import glob
import os
import string
from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

platform = env.PioPlatform()
board = env.BoardConfig()
mcu = board.get("build.mcu", "")
f_ext = board.get("build.f_ext", "")
clk_select = board.get("build.clk_select", "")
clk_select_def = {"pll":"SYSCLK_PLL","internal":"SYSCLK_OSI","external":"SYSCLK_OSE","custom":""}
SDK_DIR = platform.get_package_dir("framework-k1921vk-sdk")
DEVICE_DIR =  os.path.join(SDK_DIR,"platform","Device","NIIET",mcu)

env.Append(
    CPPPATH=[
        os.path.join(DEVICE_DIR, "Include"),
        os.path.join( SDK_DIR, "platform","CMSIS","Core","Include")
    ]
)

env.Append(
    ASFLAGS=[
        "-mthumb",
        "-mcpu=cortex-m4"
    ],

    CCFLAGS=[
        "-mthumb", 
        "-mcpu=cortex-m4",
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16",
        "-Wall",
        "-Wextra",
        "-ffunction-sections",
        "-fdata-sections",
        "-mlong-calls"

    ],

    CXXFLAGS=[
        "-std=c++11"
    ],

    CPPDEFINES=[
        ("OSECLK_VAL", str(f_ext)),# OSECLK value in Hz (0 if disconnected)
        (mcu),# MCU name
        ("MCUNAME",mcu),
        (clk_select_def[clk_select]), # SYSCLK source: PLL, OSI, OSE
    ],

    LINKFLAGS=[
        "-mthumb",
        "-mcpu=cortex-m4",
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16",
        "-mlong-calls",
        "-Wl,--gc-sections",
        "-specs=nosys.specs",
        "-specs=nano.specs",
        "-lgcc",
        "-lc"
    ],

    LIBS=["c", "gcc", "m", "stdc++"]
)

if not board.get("build.ldscript", ""):
    env.Replace(LDSCRIPT_PATH=os.path.join(DEVICE_DIR, "Source","GCC","%s.ld"%mcu))

# copy CCFLAGS to ASFLAGS (-x assembler-with-cpp mode)
#env.Append(ASFLAGS=env.get("CCFLAGS", [])[:])
