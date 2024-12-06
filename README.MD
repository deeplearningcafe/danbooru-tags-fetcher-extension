# Danbooru Tagger Extension for Automatic1111 Stable Diffusion WebUI

This extension adds a tab to the Automatic1111 Stable Diffusion WebUI that allows you to fetch tags from Danbooru.  Enter a Danbooru post ID, and the extension will retrieve and display the artist, copyright, character, and general tags associated with that post.

## Features

*   Fetches tags from Danbooru.donmai.us.
*   Displays artist, copyright, character, and general tags separately.
*   Simple and easy-to-use interface.

## Installation

1.  Download the `danbooru-tagger-extension` folder (containing `scripts/danbooru_tagger.py` and `install.py`).
2.  Place the `danbooru-tagger-extension` folder into the `extensions` folder within your Automatic1111 Stable Diffusion WebUI directory.
3.  Restart the WebUI.

or
1. Open "Extensions" tab.
2. Open "Install from URL" tab in the tab.
3. Enter https://github.com/deeplearningcafe/danbooru-tags-fetcher-extension to "URL for extension's git repository".
4. Press "Install" button.
5. Wait 5 seconds, and you will see the message "Installed into stable-diffusion-webui\extensions\danbooru-tags-fetcher-extension. Use Installed tab to restart".
6. Go to "Installed" tab, click "Check for updates", and then click "Apply and restart UI". (The next time you can also use this method to update extensions.)
7. Completely restart A1111 webui including your terminal. (If you do not know what is a "terminal", you can reboot your computer: turn your computer off and turn it on again.)


## Usage

1.  Navigate to the "Danbooru Tagger" tab in the WebUI.
2.  Enter a Danbooru post ID in the designated textbox.
3.  Click the "Get Tags" button.
4.  The extension will display the retrieved tags in the corresponding textboxes.

## Dependencies

This extension requires the `requests` and `beautifulsoup4` Python libraries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you encounter any problems or have suggestions for improvement.

## License

[Specify your license here, e.g., MIT License]
