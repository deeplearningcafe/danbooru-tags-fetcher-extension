import modules.scripts as scripts
import gradio as gr
import requests

def format_tag_string(tag_string: str) -> str:
    """
    Formats a space-separated Danbooru tag string into a comma-separated,
    human-readable format in a highly optimized way.

    This function avoids splitting the string into a list, which is slow.
    Instead, it uses a chain of optimized `replace` calls. The order of
    operations is critical:
    1. Escape parentheses to prevent them from being misinterpreted.
    2. Replace the space separators between tags with ", ".
    3. Replace underscores within tags with spaces.

    Args:
        tag_string (str): The raw, space-separated tag string.
                          e.g., "1girl long_hair star_(symbol)"

    Returns:
        str: A formatted, comma-separated string.
             e.g., "1girl, long hair, star \(symbol\)"
    """
    if pd.isna(tag_string) or not tag_string:
        return ""
    
    # The sequence of replacements is optimized for speed and correctness.
    return (
        tag_string.replace('(', r'\(')
                  .replace(')', r'\)')
                  .replace(' ', ', ')
                  .replace('_', ' ')
    )

def get_general_tags(image_id, cookies:str=None):
    # URL for the Danbooru image post
    url = f"https://danbooru.donmai.us/posts/{image_id}.json"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'} # Add User-Agent
    cookies = {'cf_clearance': cookies}
    # Download the HTML content
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code != 200:
        raise ValueError(f"Failed to retrieve the page. Status code: {response.status_code}")
    data = response.json()

    # Step 3: Extract tags by categories
    artist_tags = format_tag_string(data["tag_string_artist"])
    copyright_tags = format_tag_string(data["tag_string_copyright"])
    character_tags = format_tag_string(data["tag_string_character"])
    general_tags = format_tag_string(data["tag_string_general"])
    
    # Step 4: Prepare the result as a dictionary
    tags = {
        "Artist Tags": artist_tags,
        "Copyright Tags": copyright_tags,
        "Character Tags": character_tags,
        "General Tags": general_tags
    }
    return tags

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            danbooru_id = gr.Textbox(label="Danbooru Post ID")
            danbooru_cookie = gr.Textbox(label="Danbooru Cloudflare clearance cookie")
            submit_btn = gr.Button("Get Tags")

        with gr.Row():
            artist_tags_output = gr.Textbox(label="Artist Tags", lines=2)
            copyright_tags_output = gr.Textbox(label="Copyright Tags", lines=2)
            character_tags_output = gr.Textbox(label="Character Tags", lines=2)

        with gr.Row():
            general_tags_output = gr.Textbox(label="General Tags", lines=5)


        def process_tags(id, cookies):
            try:
                tags = get_general_tags(id, cookies)
                return (tags.get("Artist Tags",[]), tags.get("Copyright Tags",[]), tags.get("Character Tags",[]), tags.get("General Tags",[]))
            except ValueError as e:
                return ("Error: " + str(e), "", "", "")

        submit_btn.click(
            fn=process_tags,
            inputs=[danbooru_id, danbooru_cookie],
            outputs=[artist_tags_output, copyright_tags_output, character_tags_output, general_tags_output]
        )

        return [(ui_component, "Danbooru Tagger", "danbooru_tagger_tab")]


scripts.script_callbacks.on_ui_tabs(on_ui_tabs)