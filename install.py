import launch

# TODO: add pip dependency if need extra module only on extension

if not launch.is_installed("beautifulsoup4"):
    launch.run_pip("install beautifulsoup4==4.12.3", "requirements for danbooru-tagger")