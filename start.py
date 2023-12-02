from moviepy.editor import TextClip

def generate_video(video_content):
    # 동영상 생성 로직을 구현하세요. 예시로 텍스트를 포함한 동영상 생성
    clip = TextClip(video_content, fontsize=70, color='white', bg_color='black')
    clip.write_videofile("generated_video.mp4", codec="libx264")

# 예시: 폼에서 받은 내용을 사용하여 동영상 생성
form_input = "GitHub Pages에서 동영상 생성 테스트 중"
generate_video(form_input)
