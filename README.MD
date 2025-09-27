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

### 403 error
The 403 forbidden error seems to be caused by Cloudflare so we need to include the `cf_clearance` cookie in the request. To obtain it:
1.  Browse to danbooru and complete the Cloudflare captcha (if it doesn't appear try to reload/browse the page until it does).
2. Inspect the page by right clicking it and using the `inspect` or using F12 key.
3. Go to Application, Cookies and click the danbooru cookie.
4. Click the `cf_clearance` name and copy the cookie value that shows bellow, it is a long string.
5. Paste the token in the `Danbooru Cloudflare clearance cookie` textbox.

## Dependencies

This extension requires the `requests` Python library.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you encounter any problems or have suggestions for improvement.

## License

This project is licensed under the MIT license. Details are in the [LICENSE](LICENSE) file.
