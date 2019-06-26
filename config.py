import os

def can_build(env, platform):
    return platform == "x11" or platform == "windows" or platform == "osx" or platform == "android" or platform == "iphone"


def configure(env):
    if env["platform"] == "windows":
        if env["bits"] == "32":
            env.Append(LIBPATH=["#modules/fmod/api/core/lib/x86/",
                                "#modules/fmod/api/studio/lib/x86/"])       
            try:
                old_core_file = os.path.join("modules/fmod/api/core/lib/x86/", "fmod_vc.lib")
                new_core_file = os.path.join("modules/fmod/api/core/lib/x86/", "fmod_vc.windows.opt.tools.32.lib")
                os.rename(old_core_file, new_core_file)
                old_studio_file = os.path.join("modules/fmod/api/studio/lib/x86/", "fmodstudio_vc.lib")
                new_studio_file = os.path.join("modules/fmod/api/studio/lib/x86/", "fmodstudio_vc.windows.opt.tools.32.lib")
                os.rename(old_studio_file, new_studio_file)
            except:
                print("Fmod libraries already renamed")
            env.Append(LIBS=["fmod_vc", "fmodstudio_vc"])
        else:
            env.Append(LIBPATH=["#modules/fmod/api/core/lib/x64/",
                                "#modules/fmod/api/studio/lib/x64/"])               
            try:
                old_core_file = os.path.join("modules/fmod/api/core/lib/x64/", "fmod_vc.lib")
                new_core_file = os.path.join("modules/fmod/api/core/lib/x64/", "fmod_vc.windows.opt.tools.64.lib")
                os.rename(old_core_file, new_core_file)
                old_studio_file = os.path.join("modules/fmod/api/studio/lib/x64/", "fmodstudio_vc.lib")
                new_studio_file = os.path.join("modules/fmod/api/studio/lib/x64/", "fmodstudio_vc.windows.opt.tools.64.lib")
                os.rename(old_studio_file, new_studio_file)
            except:
                print("Fmod libraries already renamed")
            env.Append(LIBS=["fmod_vc", "fmodstudio_vc"])

    elif env["platform"] == "x11":
        env.Append(LIBS=["fmod", "fmodstudio"])
        if env["bits"] == "32":
            env.Append(
                LIBPATH=["#modules/fmod/api/core/lib/x86/",
                         "#modules/fmod/api/studio/lib/x86/"])
        else:
            env.Append(
                LIBPATH=["#modules/fmod/api/core/lib/x86_64/",
                         "#modules/fmod/api/studio/lib/x86_64/"])

    elif env["platform"] == "osx":
        env.Append(LIBS=["fmod", "fmodstudio"])
        env.Append(
            LIBPATH=["#modules/fmod/api/core/lib/", "#modules/fmod/api/studio/lib/"])

    elif env["platform"] == "android":
        if env["android_arch"] == "arm64v8":
            env.Append(LIBPATH=["#modules/fmod/api/core/lib/arm64-v8a", "#modules/fmod/api/studio/lib/arm64-v8a"])
        else:
            env.Append(LIBPATH=["#modules/fmod/api/core/lib/armeabi-v7a", "#modules/fmod/api/studio/lib/armeabi-v7a"])
        env.Append(LIBS=["fmod", "fmodstudio"])

    elif env["platform"] == "iphone":
        env.Append(LIBPATH=["#modules/fmod/api/core/lib/", "#modules/fmod/api/studio/lib/"])
        env.Append(LIBS=["libfmod_iphoneos.a", "libfmodstudio_iphoneos.a"])
