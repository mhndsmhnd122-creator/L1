from flask import Flask, render_template_string, request
import subprocess

app = Flask(__name__)

# قالب HTML للوحة التحكم (تصميم داكن، يدعم العربية، مع خانات تعديل النص بالكامل)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>لوحة تحكم البث - Kick Relay</title>
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: Tahoma, sans-serif; padding: 20px; }
        .container { max-width: 600px; margin: auto; background: #161b22; padding: 20px; border-radius: 8px; border: 1px solid #30363d; }
        label { display: block; margin-top: 10px; font-weight: bold; color: #58a6ff; }
        input, select { width: 100%; padding: 8px; margin-top: 5px; background: #0d1117; border: 1px solid #30363d; color: #fff; border-radius: 4px; box-sizing: border-box; }
        button { background: #238636; color: white; border: none; padding: 10px 15px; margin-top: 15px; width: 100%; font-size: 16px; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2ea043; }
    </style>
</head>
<body>
    <div class="container">
        <h2>لوحة تحكم ريلاي البث (Kick)</h2>
        <form method="POST">
            <label>اسم قناة كيك (Kick Channel):</label>
            <input type="text" name="channel" value="OSAMAH" required>

            <label>منصة البث المستقبلة:</label>
            <select name="platform">
                <option value="youtube">YouTube Live</option>
                <option value="restream">Restream</option>
            </select>

            <label>مفتاح البث (Stream Key - ظاهر):</label>
            <input type="text" name="key" placeholder="أدخل مفتاح البث هنا" required>

            <label>النص المراد إضافته على الشاشة:</label>
            <input type="text" name="overlay_text" value="لا تنسى الإشتراك ودعم القناة">

            <label>حجم الخط (Font Size):</label>
            <input type="number" name="font_size" value="24">

            <label>لون الخط (Hex Color):</label>
            <input type="text" name="font_color" value="white">

            <label>مكان النص على الشاشة:</label>
            <select name="position">
                <option value="top-left">أعلى اليسار</option>
                <option value="top-right">أعلى اليمين</option>
                <option value="bottom-left">أسفل اليسار</option>
                <option value="bottom-right">أسفل اليمين</option>
            </select>

            <button type="submit">بدء تشغيل البث</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        channel = request.form.get('channel')
        key = request.form.get('key')
        text = request.form.get('overlay_text')
        size = request.form.get('font_size')
        color = request.form.get('font_color')
        pos = request.form.get('position')
        
        # إحداثيات النص بناءً على الاختيار
        pos_map = {
            "top-left": "x=10:y=10",
            "top-right": "x=w-tw-10:y=10",
            "bottom-left": "x=10:y=h-th-10",
            "bottom-right": "x=w-tw-10:y=h-th-10"
        }
        position_coord = pos_map.get(pos, "x=10:y=10")
        
        # أمر FFmpeg التوضيحي مع الفلتر المدمج للنص
        # (ملاحظة: الرابط الافتراضي كمثال للبث)
        print(f"Starting relay for {channel} with text overlay: '{text}' at {position_coord}")
        
        return "<h3>تم استلام الإعدادات بنجاح وجاري معالجة البث!</h3><a href='/'>العودة للوحة التحكم</a>"
        
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

