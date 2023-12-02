from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class VideoForm(FlaskForm):
    content = StringField('Content')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = VideoForm()

    if form.validate_on_submit():
        content = form.content.data
      
def create_video(content):
    image = Image.new('RGB', (500, 500), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    draw.text((10, 10), content, font=font, fill='black')

    image.save('output_video.gif', save_all=True, duration=1000, loop=0)

# 위의 코드에서 동영상을 생성하는 부분에 아래 코드를 추가합니다.
# content 변수는 폼에서 입력한 내용입니다.
# create_video(content)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
