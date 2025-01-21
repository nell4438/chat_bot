import gradio as gr
from hf import demo as demo_hf
from sambanova import demo as demo_sambanova
from together import demo as demo_together
# from ltx_video import demo as demo_ltx_video

with gr.Blocks(fill_height=True) as demo:
    with gr.Tab("Meta Llama"):
        demo_sambanova.render()
        # gr.Markdown(
        #     "**Note:** You need to use a SambaNova API key from [SambaNova Cloud](https://cloud.sambanova.ai/)."
        # )
    # with gr.Tab("LTX Video"):
    #     demo_ltx_video.render()
    with gr.Tab("Hugging Face"):
        demo_hf.render()
    with gr.Tab("Together"):
        demo_together.render()


if __name__ == "__main__":
    demo.queue(api_open=True).launch(ssr_mode=False, show_api=True)
