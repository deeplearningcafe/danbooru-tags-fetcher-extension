import launch

# TODO: add pip dependency if need extra module only on extension

if not launch.is_installed("requests"):
    launch.run_pip("install requests curl_cffi", "requirements for danbooru-tagger")
