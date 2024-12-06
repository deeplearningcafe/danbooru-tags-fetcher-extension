import modules.scripts as scripts
import gradio as gr
import requests
from bs4 import BeautifulSoup

def get_general_tags(image_id):
    # URL for the Danbooru image post
    url = f"https://danbooru.donmai.us/posts/{image_id}"
    
    # Download the HTML content
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Step 2: Define a helper function to extract tags from specific categories
    def extract_tags(category_class):
        category_tags = []
        tag_list = soup.find("ul", class_=category_class)
        if tag_list:
            tags = tag_list.find_all("li", {"data-tag-name": True})
            category_tags = [tag['data-tag-name'].replace("_", " ") for tag in tags]
        return ", ".join(category_tags)
    
    # Step 3: Extract tags by categories
    artist_tags = extract_tags("artist-tag-list")
    copyright_tags = extract_tags("copyright-tag-list")
    character_tags = extract_tags("character-tag-list")
    general_tags = extract_tags("general-tag-list")
    
    # Step 4: Prepare the result as a dictionary
    tags = {
        "Artist Tags": artist_tags,
        "Copyright Tags": copyright_tags,
        "Character Tags": character_tags,
        "General Tags": general_tags
    }
    return tags


# def on_ui_tabs():
#     with gr.Blocks(analytics_enabled=False) as ui_component:
#         with gr.Row():
#             danbooru_id = gr.Textbox(label="Danbooru Post ID")
#             output = gr.Textbox(label="General Tags", lines=5)
#             submit_btn = gr.Button("Get Tags")

#             def process_tags(id):
#                 try:
#                     tags = get_general_tags(id)
#                     return tags
#                 except ValueError as e:
#                     return f"Error: {e}"

#             submit_btn.click(fn=process_tags, inputs=[danbooru_id], outputs=[output])

#         return [(ui_component, "Danbooru Tagger", "danbooru_tagger_tab")]
def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            danbooru_id = gr.Textbox(label="Danbooru Post ID")
            submit_btn = gr.Button("Get Tags")

        with gr.Row():
            artist_tags_output = gr.Textbox(label="Artist Tags", lines=2)
            copyright_tags_output = gr.Textbox(label="Copyright Tags", lines=2)
            character_tags_output = gr.Textbox(label="Character Tags", lines=2)

        with gr.Row():
            general_tags_output = gr.Textbox(label="General Tags", lines=5)


        def process_tags(id):
            try:
                tags = get_general_tags(id)
                return (tags.get("Artist Tags",[]), tags.get("Copyright Tags",[]), tags.get("Character Tags",[]), tags.get("General Tags",[]))
            except ValueError as e:
                return ("Error: " + str(e), "", "", "")

        submit_btn.click(
            fn=process_tags,
            inputs=[danbooru_id],
            outputs=[artist_tags_output, copyright_tags_output, character_tags_output, general_tags_output]
        )

        return [(ui_component, "Danbooru Tagger", "danbooru_tagger_tab")]


scripts.script_callbacks.on_ui_tabs(on_ui_tabs)